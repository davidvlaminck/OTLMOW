# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusSoortvoertuig(KeuzelijstField):
    """Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren."""
    naam = 'KlVriLusSoortvoertuig'
    label = 'VRI-lus soort voertuig'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusSoortvoertuig'
    definition = 'Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusSoortvoertuig'
    options = {
        'fiets': KeuzelijstWaarde(invulwaarde='fiets',
                                  label='fiets',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/fiets'),
        'motor': KeuzelijstWaarde(invulwaarde='motor',
                                  label='motor',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/motor'),
        'voertuig': KeuzelijstWaarde(invulwaarde='voertuig',
                                     label='voertuig',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/voertuig')
    }

