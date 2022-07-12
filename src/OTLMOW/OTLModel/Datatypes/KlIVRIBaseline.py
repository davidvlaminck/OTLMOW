# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIBaseline(KeuzelijstField):
    """De specificatieversie van het protocol van de iVRI component."""
    naam = 'KlIVRIBaseline'
    label = 'iVRIBaseline'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlIVRIBaseline'
    definition = 'De specificatieversie van het protocol van de iVRI component.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIBaseline'
    options = {
        'idd-tlc-fi-version-1-3-1': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-1-3-1',
                                                     label='IDD TLC-FI version 1.3.1',
                                                     status='ingebruik',
                                                     definitie='IDD TLC-FI version 1.3.1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-3-1')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlIVRIBaseline.get_dummy_data()

