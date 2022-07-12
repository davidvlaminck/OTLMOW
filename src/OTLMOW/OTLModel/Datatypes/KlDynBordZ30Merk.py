# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordZ30Merk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordZ30Merk'
    label = 'Z30 merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordZ30Merk'
    definition = 'Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordZ30Merk'
    options = {
        'Futurit': KeuzelijstWaarde(invulwaarde='Futurit',
                                    label='Futurit',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Futurit'),
        'Q-lite': KeuzelijstWaarde(invulwaarde='Q-lite',
                                   label='Q-lite',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Q-lite')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordZ30Merk.get_dummy_data()

