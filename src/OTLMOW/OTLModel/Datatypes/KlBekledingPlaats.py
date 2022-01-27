# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBekledingPlaats(KeuzelijstField):
    """Mogelijke locaties van de bekleding op de buis of put."""
    naam = 'KlBekledingPlaats'
    label = 'Bekleding plaats'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBekledingPlaats'
    definition = 'Mogelijke locaties van de bekleding op de buis of put.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBekledingPlaats'
    options = {
        'inwendig': KeuzelijstWaarde(invulwaarde='inwendig',
                                     label='inwendig',
                                     definitie='binnenzijde van de buis/put, waar deze in contact staat met het medium dat door de buis/put wordt getransporteerd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/inwendig'),
        'uitwendig': KeuzelijstWaarde(invulwaarde='uitwendig',
                                      label='uitwendig',
                                      definitie='buitenzijde van de buis/put, waar deze in contact staat met de omgeving',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBekledingPlaats/uitwendig')
    }

