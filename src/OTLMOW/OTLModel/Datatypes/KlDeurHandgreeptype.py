# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDeurHandgreeptype(KeuzelijstField):
    """Types handgrepen van deuren."""
    naam = 'KlDeurHandgreeptype'
    label = 'Deur handgreeptype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlDeurHandgreeptype'
    definition = 'Types handgrepen van deuren.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDeurHandgreeptype'
    options = {
        'handvat': KeuzelijstWaarde(invulwaarde='handvat',
                                    label='handvat',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/handvat'),
        'hendel-RWS': KeuzelijstWaarde(invulwaarde='hendel-RWS',
                                       label='hendel RWS',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/hendel-RWS'),
        'klink': KeuzelijstWaarde(invulwaarde='klink',
                                  label='klink',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDeurHandgreeptype/klink')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDeurHandgreeptype.get_dummy_data()

