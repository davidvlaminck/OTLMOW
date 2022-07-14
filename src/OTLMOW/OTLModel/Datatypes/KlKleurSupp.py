# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurSupp(KeuzelijstField):
    """Keuzelijst om de kleur van de toegevoegde supplementen van de verharding te bepalen."""
    naam = 'KlKleurSupp'
    label = 'Kleur supplementen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurSupp'
    definition = 'Keuzelijst om de kleur van de toegevoegde supplementen van de verharding te bepalen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurSupp'
    options = {
        'beige': KeuzelijstWaarde(invulwaarde='beige',
                                  label='beige',
                                  status='ingebruik',
                                  definitie='De kleur rood.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/beige'),
        'bordeaux-bruin': KeuzelijstWaarde(invulwaarde='bordeaux-bruin',
                                           label='bordeaux-bruin',
                                           status='ingebruik',
                                           definitie='De kleur bordeaux/bruin.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/bordeaux-bruin'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='ingebruik',
                                 definitie='Geen of standaard kleur.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/geen'),
        'oker': KeuzelijstWaarde(invulwaarde='oker',
                                 label='oker',
                                 status='ingebruik',
                                 definitie='De kleur oker.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/oker'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='ingebruik',
                                 definitie='De kleur beige.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/rood')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

