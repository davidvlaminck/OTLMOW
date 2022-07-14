# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEMarkeringSoort(KeuzelijstField):
    """Mogelijke markeringsoorten op een lijvormig element."""
    naam = 'KlLEMarkeringSoort'
    label = 'Soort markering van lijnvormig element'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEMarkeringSoort'
    definition = 'Mogelijke markeringsoorten op een lijvormig element.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEMarkeringSoort'
    options = {
        'biggenrug': KeuzelijstWaarde(invulwaarde='biggenrug',
                                      label='biggenrug',
                                      status='ingebruik',
                                      definitie='Een betonnen obstakel dat meestal een infrastructurele en beschermende functie heeft',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/biggenrug'),
        'boordsteen': KeuzelijstWaarde(invulwaarde='boordsteen',
                                       label='boordsteen',
                                       status='ingebruik',
                                       definitie='Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen'),
        'boordsteen-parkeerverbod': KeuzelijstWaarde(invulwaarde='boordsteen-parkeerverbod',
                                                     label='boordsteen parkeerverbod',
                                                     status='ingebruik',
                                                     definitie='Een lijnvormig element dat de scheiding verzorgt tussen een rijbaan en het meestal hoger gelegen trottoir met als functie het aanduiden van parkeerverbod',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/boordsteen-parkeerverbod'),
        'new-Jersey': KeuzelijstWaarde(invulwaarde='new-Jersey',
                                       label='new Jersey',
                                       status='ingebruik',
                                       definitie='Een afschermende constructie uit kunststof, beton of metaal dat naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/new-Jersey'),
        'vangrail': KeuzelijstWaarde(invulwaarde='vangrail',
                                     label='vangrail',
                                     status='ingebruik',
                                     definitie='Een afschermende constructie die naast wegen wordt geplaatst om te voorkomen dat voertuigen de weg in zijdelingse richting verlaten, kantelen of de middenberm doorkruisen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEMarkeringSoort/vangrail')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

