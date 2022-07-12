# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCOpeningType(KeuzelijstField):
    """Types van opening."""
    naam = 'KlLEGCOpeningType'
    label = 'Opening type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCOpeningType'
    definition = 'Types van opening.'
    deprecated_version = '2.1.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpeningType'
    options = {
        'dienstopening': KeuzelijstWaarde(invulwaarde='dienstopening',
                                          label='dienstopening',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='dienstopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='nooddeur',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie="Deze optie mag niet geselecteerd worden. Indien de doorgang een nooddeur is moet het onderdeel 'Vluchtdeur' geïnstantieerd worden ipv het onderdeel 'Doorgang'.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur'),
        'sas': KeuzelijstWaarde(invulwaarde='sas',
                                label='sas',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='sas',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas'),
        'vluchtopening': KeuzelijstWaarde(invulwaarde='vluchtopening',
                                          label='vluchtopening',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='vluchtopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLEGCOpeningType.get_dummy_data()

