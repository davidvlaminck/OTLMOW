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
    def __init__(self, osloCollector: OSLOCollector):
        super().__init__(osloCollector)
        logging.info("Created an instance of OTLEnumerationCreator")
        self.osloCollector = osloCollector

    def create_block_to_write_from_enumerations(self, osloEnumeration: OSLOEnumeration):
        if not isinstance(osloEnumeration, OSLOEnumeration):
            raise ValueError(f"Input is not a OSLOEnumeration")
        if osloEnumeration.objectUri == '' or not osloEnumeration.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/'):
            raise ValueError(f"OSLOEnumeration.objectUri is invalid. Value = '{osloEnumeration.objectUri}'")
        if osloEnumeration.name == '':
            raise ValueError(f"OSLOEnumeration.name is invalid. Value = '{osloEnumeration.name}'")

        return self.create_block_to_write_from_enumeration(osloEnumeration)

    def create_block_to_write_from_enumeration(self, osloEnumeration: OSLOEnumeration):
        keuzelijst_waardes = self.get_keuzelijstwaardes_by_name(osloEnumeration.name)

        datablock = ['# coding=utf-8', 'import random',
                     'from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField']
        if len(keuzelijst_waardes) > 0:
            datablock.append('from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde')

        datablock.extend(['',
                          '',
                          f'# Generated with {self.__class__.__name__}. To modify: extend, do not edit',
                          f'class {osloEnumeration.name}(KeuzelijstField):',
                          f'    """{osloEnumeration.definition}"""',
                          f'    naam = {wrap_in_quotes(osloEnumeration.name)}',
                          f'    label = {wrap_in_quotes(osloEnumeration.label)}',
                          f'    objectUri = {wrap_in_quotes(osloEnumeration.objectUri)}',
                          f'    definition = {wrap_in_quotes(osloEnumeration.definition)}'])
        if osloEnumeration.deprecated_version != '':
            datablock.append(f'    deprecated_version = {wrap_in_quotes(osloEnumeration.deprecated_version)}')
        datablock.append(f'    codelist = {wrap_in_quotes(osloEnumeration.codelist)}')
        datablock.append('    options = {')

        for waarde in sorted(keuzelijst_waardes, key=lambda w: w.invulwaarde):
            whitespace = AbstractDatatypeCreator.get_white_space_equivalent(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(")
            datablock.append(f"        '{waarde.invulwaarde}': KeuzelijstWaarde(invulwaarde='{waarde.invulwaarde}',")
            datablock.append(f"{whitespace}label='{waarde.label}',")
            if waarde.definitie != '':
                datablock.append(f"{whitespace}definitie={wrap_in_quotes(waarde.definitie)},")
            datablock.append(f"{whitespace}objectUri='{waarde.objectUri}'),")

        if len(keuzelijst_waardes) > 0:
            datablock[-1] = datablock[-1][:-1]
        datablock.append('    }')

        # dummy values part
        datablock.append("")
        datablock.append("    @classmethod")
        datablock.append("    def get_dummy_data(cls):")
        datablock.append("        return random.choice(list(cls.options.keys()))")
        datablock.append("")
        datablock.append("    @staticmethod")
        datablock.append("    def create_dummy_data():")
        datablock.append(f"        return {osloEnumeration.name}.get_dummy_data()")

        datablock.append('')

        return datablock

    @staticmethod
    def get_graph_from_location(keuzelijstnaam):
        # create a Graph
        g = rdflib.Graph()
        keuzelijst_link = f"https://raw.githubusercontent.com/Informatievlaanderen/OSLOthema-wegenenverkeer/master/codelijsten/{keuzelijstnaam}.ttl"
        # parse the turtle file hosted on github
        try:
            g.parse(keuzelijst_link, format="turtle")
        except Exception:
            if 'KlTestKeuzelijst' in keuzelijstnaam:
                base_dir = os.path.dirname(os.path.realpath(__file__))
                keuzelijst_link = abspath(f'{base_dir}/../../../UnitTests/OTLModelCreatorTests/KlTestKeuzelijst.ttl')
                g.parse(keuzelijst_link, format="turtle")
            else:
                raise ConnectionError(f"Could not get ttl file for {keuzelijstnaam}")
        return g

    @classmethod
    def get_keuzelijstwaardes_by_name(cls, keuzelijstnaam):
        g = OTLEnumerationCreator.get_graph_from_location(keuzelijstnaam)
        return cls.get_keuzelijstwaardes_from_graph(g)

    @classmethod
    def get_keuzelijstwaardes_from_graph(cls, g: Graph):
        # get distinct set of subjects and remove the conceptschema subject
        distinct_subjects = set([str(url) for url in g.subjects()])
        scheme = next(d for d in distinct_subjects if d.startswith('https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/'))
        distinct_subjects.remove(scheme)
        # loop through each triple in the graph by subject
        lijst_keuze_opties = []
        for distinct_object in distinct_subjects:
            waarde = KeuzelijstWaarde()
            waarde.objectUri = distinct_object
            for s, p, o in g.triples((URIRef(distinct_object), None, None)):
                if str(p) == 'http://www.w3.org/2004/02/skos/core#notation':
                    waarde.invulwaarde = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#prefLabel':
                    waarde.label = str(o)
                elif str(p) == 'http://www.w3.org/2004/02/skos/core#definition':
                    waarde.definitie = str(o)
                elif str(p) == 'https://www.w3.org/ns/adms#status':
                    waarde.status = str(o)
            lijst_keuze_opties.append(waarde)
        return sorted(lijst_keuze_opties, key=lambda l: l.invulwaarde)
