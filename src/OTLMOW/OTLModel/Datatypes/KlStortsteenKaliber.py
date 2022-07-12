# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenKaliber(KeuzelijstField):
    """Mogelijke kalibers van stortsteen."""
    naam = 'KlStortsteenKaliber'
    label = 'Stortsteen kaliber'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenKaliber'
    definition = 'Mogelijke kalibers van stortsteen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenKaliber'
    options = {
        'CP-90-180A': KeuzelijstWaarde(invulwaarde='CP-90-180A',
                                       label='CP 90/180A',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='< 0,063 mm',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/CP-90-180A'),
        'CP-90-250': KeuzelijstWaarde(invulwaarde='CP-90-250',
                                      label='CP 90/250',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='< 0,063 mm',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/CP-90-250'),
        'HMA-3000-6000': KeuzelijstWaarde(invulwaarde='HMA-3000-6000',
                                          label='HMA 3000/6000',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='HMA 3000/6000',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA-3000-6000'),
        'HMA-6000-10000': KeuzelijstWaarde(invulwaarde='HMA-6000-10000',
                                           label='HMA 6000/10000',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='HMA 6000/10000',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA-6000-10000'),
        'HMA1000-3000': KeuzelijstWaarde(invulwaarde='HMA1000-3000',
                                         label='HMA1000/3000',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='HMA1000/3000',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA1000-3000'),
        'HMA10000-15000': KeuzelijstWaarde(invulwaarde='HMA10000-15000',
                                           label='HMA10000/15000',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='HMA10000/15000',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/HMA10000-15000'),
        'LMA-10-60': KeuzelijstWaarde(invulwaarde='LMA-10-60',
                                      label='LMA 10/60',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='< 0,063 mm',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-10-60'),
        'LMA-15-300': KeuzelijstWaarde(invulwaarde='LMA-15-300',
                                       label='LMA 15/300',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='LMA 15/300',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-15-300'),
        'LMA-300-1000': KeuzelijstWaarde(invulwaarde='LMA-300-1000',
                                         label='LMA 300/1000',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='LMA 300/1000',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-300-1000'),
        'LMA-40-200': KeuzelijstWaarde(invulwaarde='LMA-40-200',
                                       label='LMA 40/200',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='LMA 40/200',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-40-200'),
        'LMA-5-40': KeuzelijstWaarde(invulwaarde='LMA-5-40',
                                     label='LMA 5/40',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='< 0,063 mm',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-5-40'),
        'LMA-60-300': KeuzelijstWaarde(invulwaarde='LMA-60-300',
                                       label='LMA 60/300',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='LMA 60/300',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/LMA-60-300'),
        'groter-dan-125-mm': KeuzelijstWaarde(invulwaarde='groter-dan-125-mm',
                                              label='groter dan 125 mm',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='> 125 mm',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/groter-dan-125-mm'),
        'kleiner-dan-0.063-mm': KeuzelijstWaarde(invulwaarde='kleiner-dan-0.063-mm',
                                                 label='kleiner dan 0.063 mm',
                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='< 0,063 mm',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/kleiner-dan-0.063-mm'),
        'korrelmaal-14-20': KeuzelijstWaarde(invulwaarde='korrelmaal-14-20',
                                             label='korrelmaal 14/20',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='korrelmaal 14/20',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaal-14-20'),
        'korrelmaat-20-31.5': KeuzelijstWaarde(invulwaarde='korrelmaat-20-31.5',
                                               label='korrelmaat 20/31.5',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='korrelmaat 20/31.5',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaat-20-31.5'),
        'korrelmaat-31.5-63': KeuzelijstWaarde(invulwaarde='korrelmaat-31.5-63',
                                               label='korrelmaat 31.5/63',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='korrelmaat 31.5/63',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenKaliber/korrelmaat-31.5-63')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlStortsteenKaliber.get_dummy_data()

