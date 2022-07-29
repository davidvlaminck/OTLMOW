# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVGOpstelling(KeuzelijstField):
    """Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn."""
    naam = 'KlVGOpstelling'
    label = 'Vlak geluidschermelement opstelling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVGOpstelling'
    definition = 'Beschrijft de oriëntatie van het geplaatste schermelement tov de weg. De oriëntatie van vlakke schermen kan naast loodrecht op het maaiveld ook schuin naar achter hellend of schuin naar voor hellend zijn.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVGOpstelling'
    options = {
        'loodrecht-op-maaiveld': KeuzelijstWaarde(invulwaarde='loodrecht-op-maaiveld',
                                                  label='loodrecht op maaiveld',
                                                  status='ingebruik',
                                                  definitie='loodrecht op maaiveld',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/loodrecht-op-maaiveld'),
        'schuin-naar-achter-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-achter-hellend',
                                                       label='schuin naar achter hellend',
                                                       status='ingebruik',
                                                       definitie='schuin naar achter hellend t.o.v. de weg',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-achter-hellend'),
        'schuin-naar-voor-hellend': KeuzelijstWaarde(invulwaarde='schuin-naar-voor-hellend',
                                                     label='schuin naar voor hellend',
                                                     status='ingebruik',
                                                     definitie='schuin naar voor hellend t.o.v. de weg',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVGOpstelling/schuin-naar-voor-hellend')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

