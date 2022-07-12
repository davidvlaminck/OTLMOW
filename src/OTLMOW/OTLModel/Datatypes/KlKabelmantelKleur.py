# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmantelKleur(KeuzelijstField):
    """Lijst van mogelijke kleuren voor de kabelmantel."""
    naam = 'KlKabelmantelKleur'
    label = 'Kabelmantel kleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlKabelmantelKleur'
    definition = 'Lijst van mogelijke kleuren voor de kabelmantel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmantelKleur'
    options = {
        'blank-koper': KeuzelijstWaarde(invulwaarde='blank-koper',
                                        label='blank koper',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blank-koper'),
        'blauw': KeuzelijstWaarde(invulwaarde='blauw',
                                  label='blauw',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/blauw'),
        'geel-grijs': KeuzelijstWaarde(invulwaarde='geel-grijs',
                                       label='geel-grijs',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-grijs'),
        'geel-groen': KeuzelijstWaarde(invulwaarde='geel-groen',
                                       label='geel-groen',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-groen'),
        'geel-of-zwart': KeuzelijstWaarde(invulwaarde='geel-of-zwart',
                                          label='geel of zwart',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-of-zwart'),
        'geel-zwart': KeuzelijstWaarde(invulwaarde='geel-zwart',
                                       label='geel-zwart',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/geel-zwart'),
        'grijs': KeuzelijstWaarde(invulwaarde='grijs',
                                  label='grijs',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/grijs'),
        'groen-met-4-zwarte-strepen': KeuzelijstWaarde(invulwaarde='groen-met-4-zwarte-strepen',
                                                       label='groen met 4 zwarte strepen',
                                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-met-4-zwarte-strepen'),
        'groen-zwart': KeuzelijstWaarde(invulwaarde='groen-zwart',
                                        label='groen-zwart',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/groen-zwart'),
        'onbekend': KeuzelijstWaarde(invulwaarde='onbekend',
                                     label='onbekend',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/onbekend'),
        'oranje': KeuzelijstWaarde(invulwaarde='oranje',
                                   label='oranje',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/oranje'),
        'rood': KeuzelijstWaarde(invulwaarde='rood',
                                 label='rood',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood'),
        'rood-wit': KeuzelijstWaarde(invulwaarde='rood-wit',
                                     label='rood-wit',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/rood-wit'),
        'transparant': KeuzelijstWaarde(invulwaarde='transparant',
                                        label='transparant',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/transparant'),
        'yp': KeuzelijstWaarde(invulwaarde='yp',
                               label='YP',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/yp'),
        'zwart': KeuzelijstWaarde(invulwaarde='zwart',
                                  label='zwart',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart'),
        'zwart-rood': KeuzelijstWaarde(invulwaarde='zwart-rood',
                                       label='zwart-rood',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmantelKleur/zwart-rood')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlKabelmantelKleur.get_dummy_data()

