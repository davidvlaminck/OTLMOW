# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerBoomvorm(KeuzelijstField):
    """Behandelingswijzen van bomen."""
    naam = 'KlBeheerBoomvorm'
    label = 'Beheer boomvorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerBoomvorm'
    definition = 'Behandelingswijzen van bomen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerBoomvorm'
    options = {
        'afzagen-boompalen': KeuzelijstWaarde(invulwaarde='afzagen-boompalen',
                                              label='afzagen boompalen',
                                              definitie='Afzagen van boompalen van boompaalconstructies.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/afzagen-boompalen'),
        'anti-wortelscherm': KeuzelijstWaarde(invulwaarde='anti-wortelscherm',
                                              label='anti-wortelscherm',
                                              definitie='Plaatsen van anti-wortel scherm in de grond onder een boom.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/anti-wortelscherm'),
        'begeleidingssnoei': KeuzelijstWaarde(invulwaarde='begeleidingssnoei',
                                              label='begeleidingssnoei',
                                              definitie='Begeleidingssnoei van bomen.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begeleidingssnoei'),
        'begieten': KeuzelijstWaarde(invulwaarde='begieten',
                                     label='begieten',
                                     definitie='Periodisch begieten van bomen.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begieten'),
        'bodemafdekking': KeuzelijstWaarde(invulwaarde='bodemafdekking',
                                           label='bodemafdekking',
                                           definitie='Bodemafdekking van de grond rond bomen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodemafdekking'),
        'bodembeluchting-luchtinjectie': KeuzelijstWaarde(invulwaarde='bodembeluchting-luchtinjectie',
                                                          label='bodembeluchting-luchtinjectie',
                                                          definitie='Bodembeluchting-luchtinjectie van de grond rond bomen.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodembeluchting-luchtinjectie'),
        'boren-grondpijler': KeuzelijstWaarde(invulwaarde='boren-grondpijler',
                                              label='boren grondpijler',
                                              definitie='Boren van een grondpijler in de grond rond de boom.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/boren-grondpijler'),
        'dynamische-kroonverankering': KeuzelijstWaarde(invulwaarde='dynamische-kroonverankering',
                                                        label='dynamische kroonverankering',
                                                        definitie='dynamische kroonverankering van een boom.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/dynamische-kroonverankering'),
        'gedeeltelijk-ontstronken': KeuzelijstWaarde(invulwaarde='gedeeltelijk-ontstronken',
                                                     label='gedeeltelijk ontstronken',
                                                     definitie='Gedeeltelijk ontstronken van bomen.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gedeeltelijk-ontstronken'),
        'gronduitwisseling-wortelzone': KeuzelijstWaarde(invulwaarde='gronduitwisseling-wortelzone',
                                                         label='gronduitwisseling wortelzone',
                                                         definitie='Gronduitwisseling wortelzone van de grond rond bomen.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gronduitwisseling-wortelzone'),
        'kandelaren': KeuzelijstWaarde(invulwaarde='kandelaren',
                                       label='kandelaren',
                                       definitie='Kandelaren van bomen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kandelaren'),
        'knotten': KeuzelijstWaarde(invulwaarde='knotten',
                                    label='knotten',
                                    definitie='Knotten van bomen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/knotten'),
        'kroonreductie': KeuzelijstWaarde(invulwaarde='kroonreductie',
                                          label='kroonreductie',
                                          definitie='Kroonreductie van bomen.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kroonreductie'),
        'leiboomsnoei': KeuzelijstWaarde(invulwaarde='leiboomsnoei',
                                         label='leiboomsnoei',
                                         definitie='Leiboomsnoei van bomen.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/leiboomsnoei'),
        'onderhoudssnoei': KeuzelijstWaarde(invulwaarde='onderhoudssnoei',
                                            label='onderhoudssnoei',
                                            definitie='Onderhoudssnoei van bomen.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/onderhoudssnoei'),
        'rooien': KeuzelijstWaarde(invulwaarde='rooien',
                                   label='rooien',
                                   definitie='Rooien van bomen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/rooien'),
        'scheren': KeuzelijstWaarde(invulwaarde='scheren',
                                    label='scheren',
                                    definitie='Scheren van bomen.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/scheren'),
        'stam--en-takbescherming': KeuzelijstWaarde(invulwaarde='stam--en-takbescherming',
                                                    label='stam- en takbescherming',
                                                    definitie='Stam- en takbescherming van bomen.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stam--en-takbescherming'),
        'stambescherming-zonnebrand': KeuzelijstWaarde(invulwaarde='stambescherming-zonnebrand',
                                                       label='stambescherming zonnebrand',
                                                       definitie='Bescherming van de stam van bomen tegen zonnebrand.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stambescherming-zonnebrand'),
        'statische-kroonverankering': KeuzelijstWaarde(invulwaarde='statische-kroonverankering',
                                                       label='statische kroonverankering',
                                                       definitie='Statische kroonverankering van een boom.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/statische-kroonverankering'),
        'vellen': KeuzelijstWaarde(invulwaarde='vellen',
                                   label='vellen',
                                   definitie='Vellen van bomen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vellen'),
        'verplanten': KeuzelijstWaarde(invulwaarde='verplanten',
                                       label='verplanten',
                                       definitie='Verplanten van bomen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verplanten'),
        'verwijderen-boompalen': KeuzelijstWaarde(invulwaarde='verwijderen-boompalen',
                                                  label='verwijderen boompalen',
                                                  definitie='Verwijderen van boompalen van boompaalconstructies.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-boompalen'),
        'verwijderen-gietrand': KeuzelijstWaarde(invulwaarde='verwijderen-gietrand',
                                                 label='verwijderen gietrand',
                                                 definitie='Verwijderen van de gietrand die soms aangelegd wordt rond de basis van bomen.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-gietrand'),
        'volledig-ontstronken': KeuzelijstWaarde(invulwaarde='volledig-ontstronken',
                                                 label='volledig ontstronken',
                                                 definitie='Volledig ontstronken van bomen.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/volledig-ontstronken'),
        'vormsnoei': KeuzelijstWaarde(invulwaarde='vormsnoei',
                                      label='vormsnoei',
                                      definitie='Vormsnoei van bomen.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vormsnoei'),
        'wegnemen-waterloten-en-wortelopslag': KeuzelijstWaarde(invulwaarde='wegnemen-waterloten-en-wortelopslag',
                                                                label='wegnemen waterloten en wortelopslag',
                                                                definitie='Wegnemen van waterloten en wortelopslag van bomen.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/wegnemen-waterloten-en-wortelopslag')
    }

