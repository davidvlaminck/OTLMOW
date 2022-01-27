# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRackType(KeuzelijstField):
    """Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder."""
    naam = 'KlRackType'
    label = 'rack type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRackType'
    definition = 'Lijst met gestandaardiseerde en niet-gestandaardiseerde types rack in gebruik bij de assetbeheerder.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRackType'
    options = {
        '19-inch': KeuzelijstWaarde(invulwaarde='19-inch',
                                    label='19-inch',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/19-inch'),
        '21-inch': KeuzelijstWaarde(invulwaarde='21-inch',
                                    label='21-inch',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/21-inch'),
        'DIN-rail': KeuzelijstWaarde(invulwaarde='DIN-rail',
                                     label='DIN-rail',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/DIN-rail'),
        'MIVLVERack': KeuzelijstWaarde(invulwaarde='MIVLVERack',
                                       label='MIVLVERack',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVLVERack'),
        'MIVSATRack': KeuzelijstWaarde(invulwaarde='MIVSATRack',
                                       label='MIVSATRack',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRackType/MIVSATRack')
    }

