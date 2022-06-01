# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierWerking(KeuzelijstField):
    """Een keuzelijst met werkingsprincipes van een codeklavier."""
    naam = 'KlCodeklavierWerking'
    label = 'Codeklavier werking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierWerking'
    definition = 'Een keuzelijst met werkingsprincipes van een codeklavier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierWerking'
    options = {
        'cijfercodeslot': KeuzelijstWaarde(invulwaarde='cijfercodeslot',
                                           label='cijfercodeslot',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot'),
        'cijfercodeslot-met-drukknop': KeuzelijstWaarde(invulwaarde='cijfercodeslot-met-drukknop',
                                                        label='cijfercodeslot met drukknop',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot-met-drukknop'),
        'drukknop': KeuzelijstWaarde(invulwaarde='drukknop',
                                     label='drukknop',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/drukknop')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlCodeklavierWerking.get_dummy_data()

