# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStopcontactAantalPolen(KeuzelijstField):
    """Mogelijke waarden voor het aantal polen van een stopcontact."""
    naam = 'KlStopcontactAantalPolen'
    label = 'stopcontact aantal polen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStopcontactAantalPolen'
    definition = 'Mogelijke waarden voor het aantal polen van een stopcontact.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStopcontactAantalPolen'
    options = {
        '3P': KeuzelijstWaarde(invulwaarde='3P',
                               label='3P',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/3P'),
        '4P': KeuzelijstWaarde(invulwaarde='4P',
                               label='4P',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStopcontactAantalPolen/4P')
    }

