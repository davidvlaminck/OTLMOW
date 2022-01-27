# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPlantmaatHoogte(KeuzelijstField):
    """Keuzelijst die de hoogte in centimeter gemeten van de stamvoet tot de top met een minimum en maximum waarde oplijst."""
    naam = 'KlPlantmaatHoogte'
    label = 'Plantmaat houtige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPlantmaatHoogte'
    definition = 'Keuzelijst die de hoogte in centimeter gemeten van de stamvoet tot de top met een minimum en maximum waarde oplijst.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPlantmaatHoogte'
    options = {
        '100-125': KeuzelijstWaarde(invulwaarde='100-125',
                                    label='100-125',
                                    definitie='100/125',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/100-125'),
        '125-150': KeuzelijstWaarde(invulwaarde='125-150',
                                    label='125-150',
                                    definitie='125/150',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/125-150'),
        '150-175': KeuzelijstWaarde(invulwaarde='150-175',
                                    label='150-175',
                                    definitie='150/175',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/150-175'),
        '175-200': KeuzelijstWaarde(invulwaarde='175-200',
                                    label='175-200',
                                    definitie='175/200',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/175-200'),
        '200-250': KeuzelijstWaarde(invulwaarde='200-250',
                                    label='200-250',
                                    definitie='200/250',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/200-250'),
        '250-300': KeuzelijstWaarde(invulwaarde='250-300',
                                    label='250-300',
                                    definitie='250/300',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/250-300'),
        '300-350': KeuzelijstWaarde(invulwaarde='300-350',
                                    label='300-350',
                                    definitie='300/350',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/300-350'),
        '350-400': KeuzelijstWaarde(invulwaarde='350-400',
                                    label='350-400',
                                    definitie='350/400',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/350-400'),
        '40-60': KeuzelijstWaarde(invulwaarde='40-60',
                                  label='40-60',
                                  definitie='40/60',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/40-60'),
        '60-80': KeuzelijstWaarde(invulwaarde='60-80',
                                  label='60-80',
                                  definitie='60/80',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/60-80'),
        '80-100': KeuzelijstWaarde(invulwaarde='80-100',
                                   label='80-100',
                                   definitie='80/100',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPlantmaatHoogte/80-100')
    }

