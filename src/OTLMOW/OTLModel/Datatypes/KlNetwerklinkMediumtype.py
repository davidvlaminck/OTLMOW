# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerklinkMediumtype(KeuzelijstField):
    """Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt."""
    naam = 'KlNetwerklinkMediumtype'
    label = 'Netwerklink mediumtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerklinkMediumtype'
    definition = 'Mogelijke waarden voor het type drager waarlangs data door de link getransporteerd wordt.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerklinkMediumtype'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een andere dan een optische, UTP, DSL of transportnetwerk verbinding.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/andere'),
        'dsl': KeuzelijstWaarde(invulwaarde='dsl',
                                label='DSL',
                                definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een DSL verbinding.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/dsl'),
        'optisch': KeuzelijstWaarde(invulwaarde='optisch',
                                    label='optisch',
                                    definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een glasvezelkabel.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/optisch'),
        'transportnetwerk': KeuzelijstWaarde(invulwaarde='transportnetwerk',
                                             label='transportnetwerk',
                                             definitie='De link tussen de netwerkpoorten wordt gerealiseerd via het optisch transportnetwerk.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/transportnetwerk'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                definitie='De link tussen de netwerkpoorten wordt gerealiseerd via een UTP kabel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerklinkMediumtype/utp')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerklinkMediumtype.get_dummy_data()

