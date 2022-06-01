# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDunneOverlagingType(KeuzelijstField):
    """Types van dunne overlaging."""
    naam = 'KlDunneOverlagingType'
    label = 'Dunne overlaging type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDunneOverlagingType'
    definition = 'Types van dunne overlaging.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDunneOverlagingType'
    options = {
        'SME-D1': KeuzelijstWaarde(invulwaarde='SME-D1',
                                   label='SME-D1',
                                   definitie='SME-D1',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D1'),
        'SME-D2': KeuzelijstWaarde(invulwaarde='SME-D2',
                                   label='SME-D2',
                                   definitie='SMA-D2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/SME-D2'),
        'antisliplaag': KeuzelijstWaarde(invulwaarde='antisliplaag',
                                         label='antisliplaag',
                                         definitie='antisliplaag',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDunneOverlagingType/antisliplaag')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDunneOverlagingType.get_dummy_data()

