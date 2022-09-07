# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethode(KeuzelijstField):
    """Manier van uitvoeren en aanbrengen van beton."""
    naam = 'KlUitvoeringsmethode'
    label = 'Uitvoeringsmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlUitvoeringsmethode'
    definition = 'Manier van uitvoeren en aanbrengen van beton.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethode'
    options = {
        'geprefabriceerd': KeuzelijstWaarde(invulwaarde='geprefabriceerd',
                                            label='Geprefabriceerd',
                                            status='ingebruik',
                                            definitie='Het beton is geprefabriceerd.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/geprefabriceerd'),
        'ter-plaatse-gestort': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort',
                                                label='Ter plaatse gestort',
                                                status='ingebruik',
                                                definitie='Het beton wordt ter plaatste gestort.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort'),
        'ter-plaatse-gestort-met-bekisting': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-met-bekisting',
                                                              label='Ter plaatse gestort met bekisting',
                                                              status='uitgebruik',
                                                              definitie='Het beton wordt ter plaatste gestort met bekisting.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-met-bekisting'),
        'ter-plaatse-gestort-zonder-bekisting': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-zonder-bekisting',
                                                                 label='Ter plaatse gestort zonder bekisting',
                                                                 status='uitgebruik',
                                                                 definitie='Het beton wordt ter plaatste gestort zonder bekisting.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-zonder-bekisting')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

