# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNazorgJaarfrequentie(KeuzelijstField):
    """Aantal keer dat jaarlijks de behandelde zone dient te worden gecontroleerd."""
    naam = 'KlNazorgJaarfrequentie'
    label = 'Nazorg jaarfrequentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlNazorgJaarfrequentie'
    definition = 'Aantal keer dat jaarlijks de behandelde zone dient te worden gecontroleerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNazorgJaarfrequentie'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              status='ingebruik',
                              definitie='Nazorg wordt 1 keer per jaar uitgevoerd.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              status='ingebruik',
                              definitie='Nazorg wordt 2 keer per jaar uitgevoerd.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              status='ingebruik',
                              definitie='Nazorg wordt 3 keer per jaar uitgevoerd.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              status='ingebruik',
                              definitie='Nazorg wordt 4 keer per jaar uitgevoerd.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/4')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

