# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConflicten(KeuzelijstField):
    """De verschillende mogelijke conflicten van een boom."""
    naam = 'KlBoomConflicten'
    label = 'Boom conflicten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConflicten'
    definition = 'De verschillende mogelijke conflicten van een boom.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConflicten'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   definitie='Andere mogelijke conflicten',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/andere'),
        'beperkte-doorwortelbare-ruimte': KeuzelijstWaarde(invulwaarde='beperkte-doorwortelbare-ruimte',
                                                           label='beperkte doorwortelbare ruimte',
                                                           status='ingebruik',
                                                           definitie='Het bodemvolume met voldoende mineralen, water en zuurstof waar de wortels van de boom zich kunnen ontwikkelen is veel lager dan verwacht',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/beperkte-doorwortelbare-ruimte'),
        'bodemverdichting': KeuzelijstWaarde(invulwaarde='bodemverdichting',
                                             label='bodemverdichting',
                                             status='ingebruik',
                                             definitie="Verdichting van de bodem door belasting (voetgangers, fietsers, auto's, bouwmaterialen,...)",
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/bodemverdichting'),
        'hinderende-takken': KeuzelijstWaarde(invulwaarde='hinderende-takken',
                                              label='hinderende takken',
                                              status='ingebruik',
                                              definitie='Takken die hinderlijk zijn voor de zichtbaarheid en de vrije doorrijhoogte of die luchtleidingen raken',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/hinderende-takken'),
        'instabiel': KeuzelijstWaarde(invulwaarde='instabiel',
                                      label='instabiel',
                                      status='ingebruik',
                                      definitie='Een boom die niet stabiel in de grond staat',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/instabiel'),
        'scheefstand': KeuzelijstWaarde(invulwaarde='scheefstand',
                                        label='scheefstand',
                                        status='ingebruik',
                                        definitie='Schuin gezakte/gegroeide boom waarbij de top van de boom in het verlengde van de stam ligt en niet verticaal opgericht is',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/scheefstand'),
        'te-dicht-bij-rand-verharding': KeuzelijstWaarde(invulwaarde='te-dicht-bij-rand-verharding',
                                                         label='te dicht bij rand verharding',
                                                         status='ingebruik',
                                                         definitie='Verharding ligt op minder dan 50 cm van de stamvoet',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/te-dicht-bij-rand-verharding'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       status='ingebruik',
                                       definitie='Een verhardingslaag bevindt zich zeer dicht tegen de boom',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/verharding'),
        'wortelopdruk': KeuzelijstWaarde(invulwaarde='wortelopdruk',
                                         label='wortelopdruk',
                                         status='ingebruik',
                                         definitie='Boomwortels die (weg)verhardingselementen opdrukken',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConflicten/wortelopdruk')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

