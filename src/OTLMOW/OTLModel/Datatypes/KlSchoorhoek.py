# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchoorhoek(KeuzelijstField):
    """De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4)."""
    naam = 'KlSchoorhoek'
    label = 'Schoorhoek'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSchoorhoek'
    definition = 'De schoorhoek van het object, uitgedrukt in 1 op x (vb.: 1/4).'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchoorhoek'
    options = {
        '1-3': KeuzelijstWaarde(invulwaarde='1-3',
                                label='1/3',
                                status='ingebruik',
                                definitie='Een schoorhoek van 1 op 3.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-3'),
        '1-4': KeuzelijstWaarde(invulwaarde='1-4',
                                label='1/4',
                                status='ingebruik',
                                definitie='Een schoorhoek van 1 op 4.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchoorhoek/1-4')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

