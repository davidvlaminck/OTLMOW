# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTsklepAfsluiterMateriaal(KeuzelijstField):
    """Materialen van de terugslagklep."""
    naam = 'KlTsklepAfsluiterMateriaal'
    label = 'Terugslagklep afsluiter materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTsklepAfsluiterMateriaal'
    definition = 'Materialen van de terugslagklep.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTsklepAfsluiterMateriaal'
    options = {
        'am---Gietijzer': KeuzelijstWaarde(invulwaarde='am---Gietijzer',
                                           label='am - Gietijzer',
                                           definitie='Een gietijzeren terugslagklep.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/am---Gietijzer'),
        'ap---Staal': KeuzelijstWaarde(invulwaarde='ap---Staal',
                                       label='ap - Staal',
                                       definitie='Een stalen terugslagklep.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/ap---Staal'),
        'av---Hdpe': KeuzelijstWaarde(invulwaarde='av---Hdpe',
                                      label='av - Hdpe',
                                      definitie='Een terugslagklep uit HDPE.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/av---Hdpe'),
        'z---Anders': KeuzelijstWaarde(invulwaarde='z---Anders',
                                       label='z - Anders',
                                       definitie='Een terugslagklep uit een ander materiaal.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTsklepAfsluiterMateriaal/z---Anders')
    }

