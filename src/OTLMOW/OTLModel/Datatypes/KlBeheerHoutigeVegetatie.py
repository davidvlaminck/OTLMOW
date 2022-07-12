# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerHoutigeVegetatie(KeuzelijstField):
    """De verschillende beheersopties voor houtige vegetatie."""
    naam = 'KlBeheerHoutigeVegetatie'
    label = 'Beheer houtige vegetatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerHoutigeVegetatie'
    definition = 'De verschillende beheersopties voor houtige vegetatie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerHoutigeVegetatie'
    options = {
        'afpalingswerken': KeuzelijstWaarde(invulwaarde='afpalingswerken',
                                            label='afpalingswerken',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Het afpalen van bepaalde oppervlaktes met vegetatie.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/afpalingswerken'),
        'begieten': KeuzelijstWaarde(invulwaarde='begieten',
                                     label='begieten',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Periodisch begieten van vegetatie. ',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/begieten'),
        'bestrijding': KeuzelijstWaarde(invulwaarde='bestrijding',
                                        label='bestrijding',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Bestrijding van ongewenste onkruiden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bestrijding'),
        'bodemafdekking-boomplaat': KeuzelijstWaarde(invulwaarde='bodemafdekking-boomplaat',
                                                     label='bodemafdekking - boomplaat',
                                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                     definitie='De bodem wordt afgedekt met een boomplaat.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-boomplaat'),
        'bodemafdekking-boomschors': KeuzelijstWaarde(invulwaarde='bodemafdekking-boomschors',
                                                      label='bodemafdekking - boomschors',
                                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                      definitie='De bodem wordt afgedekt met boomschors.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-boomschors'),
        'bodemafdekking-doek-in-jute-pla-folie': KeuzelijstWaarde(invulwaarde='bodemafdekking-doek-in-jute-pla-folie',
                                                                  label='bodemafdekking - doek in jute & PLA folie',
                                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                  definitie='De bodem wordt afgedekt met een doek in jute en PLA-folie.',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-doek-in-jute-pla-folie'),
        'bodemafdekking-groencompost': KeuzelijstWaarde(invulwaarde='bodemafdekking-groencompost',
                                                        label='bodemafdekking - groencompost',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='De bodem wordt afgedekt met groencompost.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-groencompost'),
        'bodemafdekking-houtsnippers': KeuzelijstWaarde(invulwaarde='bodemafdekking-houtsnippers',
                                                        label='bodemafdekking - houtsnippers',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='De bodem wordt afgedekt met houtsnippers.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-houtsnippers'),
        'bodemafdekking-pla-doek': KeuzelijstWaarde(invulwaarde='bodemafdekking-pla-doek',
                                                    label='bodemafdekking - PLA doek',
                                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                    definitie='De bodem wordt afgedekt met een PLA-doek.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bodemafdekking-pla-doek'),
        'dunnen': KeuzelijstWaarde(invulwaarde='dunnen',
                                   label='dunnen',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Het gelijkgronds afzagen van bomen ter bevordering van de groei van omstaande bomen of struiken.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/dunnen'),
        'gedeeltelijk-ontstronken': KeuzelijstWaarde(invulwaarde='gedeeltelijk-ontstronken',
                                                     label='gedeeltelijk ontstronken',
                                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                     definitie='Gedeeltelijk ontstronken van bomen. ',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/gedeeltelijk-ontstronken'),
        'hakhoutbeheer': KeuzelijstWaarde(invulwaarde='hakhoutbeheer',
                                          label='hakhoutbeheer',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Er wordt hakhoutbeheer uitgevoerd.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/hakhoutbeheer'),
        'hakken': KeuzelijstWaarde(invulwaarde='hakken',
                                   label='hakken',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Hakken van de grond tussen houtige vegetaties.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/hakken'),
        'maaien': KeuzelijstWaarde(invulwaarde='maaien',
                                   label='maaien',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Het maaien van de grazige vegetatie tussen de houtige vegetatie.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/maaien'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Er wordt geen beheer uitgevoerd.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/niets-doen'),
        'ontstronken': KeuzelijstWaarde(invulwaarde='ontstronken',
                                        label='ontstronken',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Ontstronken van bomen. ',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/ontstronken'),
        'rooien': KeuzelijstWaarde(invulwaarde='rooien',
                                   label='rooien',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Wegnemen van vegetatie dmv rooien. ',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/rooien'),
        'scheren': KeuzelijstWaarde(invulwaarde='scheren',
                                    label='scheren',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Het vlakvormig gelijkmatig kort afsnijden van takken van hagen, heesters en houtkanten.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/scheren'),
        'snoeien': KeuzelijstWaarde(invulwaarde='snoeien',
                                    label='snoeien',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Het inkorten of wegnemen van takken met snoeischaar of zaag.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/snoeien'),
        'spitten': KeuzelijstWaarde(invulwaarde='spitten',
                                    label='spitten',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Spitten van de grond tussen houtige vegetaties.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/spitten'),
        'wieden': KeuzelijstWaarde(invulwaarde='wieden',
                                   label='wieden',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Het wieden van de grond tussen houtige vegetaties. Dit is het verwijderen van onkruid.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/wieden')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBeheerHoutigeVegetatie.get_dummy_data()

