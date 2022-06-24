# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTestKeuzelijst(KeuzelijstField):
    """Keuzelijst met test waarden."""
    naam = 'KlTestKeuzelijst'
    label = 'Test keuzelijst'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlTestKeuzelijst'
    definition = 'Keuzelijst met test waarden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTestKeuzelijst'
    options = {
        'waarde-1': KeuzelijstWaarde(invulwaarde='waarde-1',
                                     label='waarde 1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-1'),
        'waarde-2': KeuzelijstWaarde(invulwaarde='waarde-2',
                                     label='waarde 2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-2'),
        'waarde-3': KeuzelijstWaarde(invulwaarde='waarde-3',
                                     label='waarde 3',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-3'),
        'waarde-4': KeuzelijstWaarde(invulwaarde='waarde-4',
                                     label='waarde 4',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-4'),
        'waarde-5': KeuzelijstWaarde(invulwaarde='waarde-5',
                                     label='waarde 5',
                                     status='uitgebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-5'),
        'waarde-6': KeuzelijstWaarde(invulwaarde='waarde-6',
                                     label='waarde 6',
                                     status='verwijderd',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTestKeuzelijst/waarde-6')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTestKeuzelijst.get_dummy_data()

