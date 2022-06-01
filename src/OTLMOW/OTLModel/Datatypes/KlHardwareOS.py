# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHardwareOS(KeuzelijstField):
    """vb : Windows 10 SP1, Windows 10 SP2, unix."""
    naam = 'KlHardwareOS'
    label = 'Hardware OS'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlHardwareOS'
    definition = 'vb : Windows 10 SP1, Windows 10 SP2, unix.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareOS'
    options = {
        'cent-os-linux-7-core': KeuzelijstWaarde(invulwaarde='cent-os-linux-7-core',
                                                 label='CentOS Linux 7 (Core)',
                                                 definitie='CentOS Linux 7 (Core)',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/cent-os-linux-7-core'),
        'unix': KeuzelijstWaarde(invulwaarde='unix',
                                 label='unix',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/unix'),
        'windows-10-SP1': KeuzelijstWaarde(invulwaarde='windows-10-SP1',
                                           label='windows 10 SP1',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP1'),
        'windows-10-SP2': KeuzelijstWaarde(invulwaarde='windows-10-SP2',
                                           label='windows 10 SP2',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHardwareOS/windows-10-SP2')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlHardwareOS.get_dummy_data()

