# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringSoort(KeuzelijstField):
    """Mogelijke markeringsoorten op een lijvormig element."""
    naam = 'KlLEMarkeringSoort'
    label = 'Soort markering van lijnvormig element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringSoort'
    definition = 'Mogelijke markeringsoorten op een lijvormig element.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringSoort'
    options = {
        'biggenrug': KeuzelijstWaarde(invulwaarde='biggenrug',
                                      label='biggenrug',
                                      definitie='Een betonnen obstakel dat meestal een infrastructurele en beschermende functie heeft',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/biggenrug'),
        'boordsteen': KeuzelijstWaarde(invulwaarde='boordsteen',
                                       label='boordsteen',
                                       definitie='Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen'),
        'boordsteen-parkeerverbod': KeuzelijstWaarde(invulwaarde='boordsteen-parkeerverbod',
                                                     label='boordsteen parkeerverbod',
                                                     definitie='Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir met als functie het aanduiden van parkeerverbod',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen-parkeerverbod'),
        'new-Jersey': KeuzelijstWaarde(invulwaarde='new-Jersey',
                                       label='new Jersey',
                                       definitie='Een afschermende constructie uit kunststof, beton of metaal dat naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/new-Jersey'),
        'vangrail': KeuzelijstWaarde(invulwaarde='vangrail',
                                     label='vangrail',
                                     definitie='Een afschermende constructie die naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/vangrail')
    }

