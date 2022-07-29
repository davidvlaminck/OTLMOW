# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendVerkeersbordAfwerkingsgraad(KeuzelijstField):
    """Keuzeopties om de afwerkingsgraad van een RetroreflecterendVerkeersbord aan te geven volgens SB250."""
    naam = 'KlRetroreflecterendVerkeersbordAfwerkingsgraad'
    label = 'Keuzelijst afwerkingsgraad retroreflecterend verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordAfwerkingsgraad'
    definition = 'Keuzeopties om de afwerkingsgraad van een RetroreflecterendVerkeersbord aan te geven volgens SB250.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordAfwerkingsgraad'
    options = {
        'volledig-afgewerkt': KeuzelijstWaarde(invulwaarde='volledig-afgewerkt',
                                               label='volledig afgewerkt',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordAfwerkingsgraad/volledig-afgewerkt'),
        'zonder-tekst.-symbool-of-overlay': KeuzelijstWaarde(invulwaarde='zonder-tekst.-symbool-of-overlay',
                                                             label='zonder tekst, symbool of overlay',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordAfwerkingsgraad/zonder-tekst.-symbool-of-overlay')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

