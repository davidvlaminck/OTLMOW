# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVirtueleServerMerk(KeuzelijstField):
    """Het merk van de virtuele server."""
    naam = 'KlVirtueleServerMerk'
    label = 'Virtuele server merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVirtueleServerMerk'
    definition = 'Het merk van de virtuele server.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVirtueleServerMerk'
    options = {
        'ram': KeuzelijstWaarde(invulwaarde='ram',
                                label='RAM',
                                status='ingebruik',
                                definitie='RAM',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVirtueleServerMerk/ram')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

