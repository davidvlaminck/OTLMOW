import logging
import os
from os.path import abspath

import rdflib
from rdflib import URIRef, Graph

from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLOEnumeration import OSLOEnumeration
from OTLMOW.ModelGenerator.StringHelper import wrap_in_quotes
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


class OTLEnumerationCreator(AbstractDatatypeCreator):
    default_environment = 'prd'
    most_recent_graph = None

    def __init__(self, oslo_collector: OSLOCollector):
        super().__init__(oslo_collector)
        logging.info("Created an instance of OTLEnumerationCreator")
        self.osloCollector = oslo_collector

    def create_block_to_write_from_enumerations(self, oslo_enumeration: OSLOEnumeration, environment: str = default_environment):
        if not isinstance(oslo_enumeration, OSLOEnumeration):
            raise ValueError(f"Input is not a OSLOEnumeration")
        if oslo_enumeration.objectUri == '' or not oslo_enumeration.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/'):
            raise ValueError(f"OSLOEnumeration.objectUri is invalid. Value = '{oslo_enumeration.objectUri}'")
        if oslo_enumeration.name == '':
            raise ValueError(f"OSLOEnumeration.name is invalid. Value = '{oslo_enumeration.name}'")

        return self.create_block_to_write_from_enumeration(oslo_enumeration, environment=environment)

    def create_block_to_write_from_enumeration(self, oslo_enumeration: OSLOEnumeration, environment: str = default_environment):
        keuzelijst_waardes = self.get_keuzelijstwaardes_by_name(oslo_enumeration.name, env=environment)
        adm_status = self.get_adm_status_by_name(oslo_enumeration.name, env=environment)

        datablock = ['# coding=utf-8', 'import random',
                     'from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField']
        if len(keuzelijst_waardes) > 0:
            datablock.append('from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde')

        datablock.extend(['',
                          '',
                          f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
                          f'class {oslo_enumeration.name}(KeuzelijstField):',
                          f'    """{oslo_enumeration.definition}"""',
                          f'    naam = {wrap_in_quotes(oslo_enumeration.name)}',
                          f'    label = {wrap_in_quotes(oslo_enumeration.label)}',
                          f'    objectUri = {wrap_in_quotes(oslo_enumeration.objectUri)}',
                          f'    definition = {wrap_in_quotes(oslo_enumeration.definition)}'])

        if adm_status is not None and adm_status != '':
            datablock.append(f'    status = {wrap_in_quotes(adm_status)}')
        if oslo_enumeration.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(oslo_enumeration.deprecated_version)}')
        datablock.append(f'    codelist = {wrap_in_quotes(oslo_enumeration.codelist)}')
        datablock.append('    options = {')

        for waarde in sorted(keuzelijst_waardes, key=lambda w: w.invulwaarde):
            whitespace = AbstractDatatypeCreator.get_white_space_equivalent(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(")
            datablock.append(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(invulwaarde='{waarde.invulwaarde}',")
            datablock.append(f"{whitespace}label='{waarde.label}',")
            if waarde.status != '':
                datablock.append(f"{whitespace}status='{waarde.status}',")
            if waarde.definitie != '':
                datablock.append(f"{whitespace}definitie={wrap_in_quotes(waarde.definitie)},")
            datablock.append(f"{whitespace}objectUri='{waarde.objectUri}'),")

        if len(keuzelijst_waardes) > 0:
            datablock[-1] = datablock[-1][:-1]
        datablock.append('    }')

        # dummy values part
        datablock.append("")
        datablock.append("    @classmethod")
        datablock.append("    def create_dummy_data(cls):")
        datablock.append("        return random.choice(list(map(lambda x: x.invulwaarde,")
        datablock.append("                                      "
                         "filter(lambda option: option.status == 'ingebruik', cls.options.values()))))")

        datablock.append('')

        return datablock

    @classmethod
    def get_graph_from_location(cls, keuzelijstnaam: str, env: str = default_environment):
        if env is None or env == '':
            env = cls.default_environment

        if env == 'prd':
            env = 'master'
        elif env == 'tei':
            env = 'test'

        # create a Graph
        g = rdflib.Graph()
        keuzelijst_link = f"https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/{env}/codelijsten/{keuzelijstnaam}.ttl"

        # parse the turtle file hosted on github
        try:
            g.parse(keuzelijst_link, format="turtle")
        except Exception as exc:
            if 'KlTestKeuzelijst' in keuzelijstnaam:
                base_dir = os.path.dirname(os.path.realpath(__file__))
                keuzelijst_link = abspath(f'{base_dir}/../../../UnitTests/OTLModelCreatorUnitTests/KlTestKeuzelijst.ttl')
                g.parse(keuzelijst_link, format="turtle")
            else:
                logging.error(f"Could not get ttl file for {keuzelijstnaam}")
                raise exc
        OTLEnumerationCreator.most_recent_graph = (keuzelijstnaam, env, g)
        return g

    @classmethod
    def get_graph(cls, keuzelijstnaam: str, env: str = default_environment):
        # check if the most_recent_graph holds the correct graph. If so, return that one, else fetch the correct one
        if OTLEnumerationCreator.most_recent_graph is not None:
            recent_naam, recent_env, recent_graph = OTLEnumerationCreator.most_recent_graph
            if recent_naam == keuzelijstnaam and recent_env == env:
                return recent_graph
        return OTLEnumerationCreator.get_graph_from_location(keuzelijstnaam=keuzelijstnaam, env=env)

    @classmethod
    def get_keuzelijstwaardes_by_name(cls, keuzelijstnaam: str, env: str = default_environment) -> [KeuzelijstWaarde]:
        g = OTLEnumerationCreator.get_graph(keuzelijstnaam, env)
        return cls.get_keuzelijstwaardes_from_graph(g, env)

    @classmethod
    def get_keuzelijstwaardes_from_graph(cls, g: Graph, env: str = default_environment):
        lijst_keuze_opties = []

        subjects = set(g.subjects(predicate=None, object=None))
        distinct_subjects_list = sorted(subjects, key=lambda x: str(x))

        for distinct_subject in distinct_subjects_list:
            subject_str = str(distinct_subject)
            if subject_str.startswith('https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/'):
                continue
            elif env == 'tei' and subject_str.startswith('https://wegenenverkeer-test.data.vlaanderen.be/id/conceptscheme/'):
                continue
            waarde = KeuzelijstWaarde()
            waarde.objectUri = subject_str
            status = g.value(subject=distinct_subject, predicate=URIRef('https://www.w3.org/ns/adms#status'))
            if status is not None:
                waarde.status = str(status).replace('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/', '')
            waarde.invulwaarde = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#notation')))
            waarde.definitie = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#definition')))
            waarde.label = str(
                g.value(subject=distinct_subject, predicate=URIRef('http://www.w3.org/2004/02/skos/core#prefLabel')))
            lijst_keuze_opties.append(waarde)

        return lijst_keuze_opties

    @classmethod
    def get_adm_status_by_name(cls, keuzelijstnaam: str, env: str = default_environment) -> str:
        g = OTLEnumerationCreator.get_graph(keuzelijstnaam, env=env)
        return cls.get_adm_status_from_graph(g, name=keuzelijstnaam, env=env)

    @classmethod
    def get_adm_status_from_graph(cls, g: Graph, name: str, env: str = default_environment) -> str:
        scheme_uri = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/' + name
        if env == 'tei':
            scheme_uri = 'https://wegenenverkeer-test.data.vlaanderen.be/id/conceptscheme/' + name

        status = g.value(subject=URIRef(scheme_uri), predicate=URIRef('https://www.w3.org/ns/adms#status'))

        if status is not None:
            return str(status).replace('https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/', '')
        else:
            return ''
