# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBekledingPlaats(KeuzelijstField):
    """Mogelijke locaties van de bekleding op de buis of put."""
    naam = 'KlBekledingPlaats'
    label = 'Bekleding plaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBekledingPlaats'
    definition = 'Mogelijke locaties van de bekleding op de buis of put.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBekledingPlaats'
    options = {
        'inwendig': KeuzelijstWaarde(invulwaarde='inwendig',
                                     label='inwendig',
                                     status='ingebruik',
                                     definitie='binnenzijde van de buis/put, waar deze in contact staat met het medium dat door de buis/put wordt getransporteerd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/inwendig'),
        'uitwendig': KeuzelijstWaarde(invulwaarde='uitwendig',
                                      label='uitwendig',
                                      status='ingebruik',
                                      definitie='buitenzijde van de buis/put, waar deze in contact staat met de omgeving',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/uitwendig')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

