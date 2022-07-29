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
    status = 'ingebruik'
    deprecated_version = '2.1.0'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCOpeningType'
    options = {
        'dienstopening': KeuzelijstWaarde(invulwaarde='dienstopening',
                                          label='dienstopening',
                                          status='ingebruik',
                                          definitie='dienstopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='nooddeur',
                                     status='ingebruik',
                                     definitie="Deze optie mag niet geselecteerd worden. Indien de doorgang een nooddeur is moet het onderdeel 'Vluchtdeur' geïnstantieerd worden ipv het onderdeel 'Doorgang'.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur'),
        'sas': KeuzelijstWaarde(invulwaarde='sas',
                                label='sas',
                                status='ingebruik',
                                definitie='sas',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas'),
        'vluchtopening': KeuzelijstWaarde(invulwaarde='vluchtopening',
                                          label='vluchtopening',
                                          status='ingebruik',
                                          definitie='vluchtopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

