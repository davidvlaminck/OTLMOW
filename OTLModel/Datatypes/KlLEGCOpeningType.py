# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                          definitie='dienstopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/dienstopening'),
        'nooddeur': KeuzelijstWaarde(invulwaarde='nooddeur',
                                     label='nooddeur',
                                     definitie='Deze optie mag niet geselecteerd worden. Indien de doorgang een nooddeur is moet het onderdeel 'Vluchtdeur' geïnstantieerd worden ipv het onderdeel 'Doorgang'.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/nooddeur'),
        'sas': KeuzelijstWaarde(invulwaarde='sas',
                                label='sas',
                                definitie='sas',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/sas'),
        'vluchtopening': KeuzelijstWaarde(invulwaarde='vluchtopening',
                                          label='vluchtopening',
                                          definitie='vluchtopening',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCOpeningType/vluchtopening')
    }

