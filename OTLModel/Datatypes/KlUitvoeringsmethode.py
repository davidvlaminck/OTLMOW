# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlUitvoeringsmethode(KeuzelijstField):
    """Manier van uitvoeren en aanbrengen van beton."""
    naam = 'KlUitvoeringsmethode'
    label = 'Uitvoeringsmethode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlUitvoeringsmethode'
    definition = 'Manier van uitvoeren en aanbrengen van beton.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlUitvoeringsmethode'
    options = {
        'geprefabriceerd': KeuzelijstWaarde(invulwaarde='geprefabriceerd',
                                            label='Geprefabriceerd',
                                            definitie='Het beton is geprefabriceerd.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/geprefabriceerd'),
        'ter-plaatse-gestort-met-bekisting': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-met-bekisting',
                                                              label='Ter plaatse gestort met bekisting',
                                                              definitie='Het beton wordt ter plaatste gestort met bekisting.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-met-bekisting'),
        'ter-plaatse-gestort-zonder-bekisting': KeuzelijstWaarde(invulwaarde='ter-plaatse-gestort-zonder-bekisting',
                                                                 label='Ter plaatse gestort zonder bekisting',
                                                                 definitie='Het beton wordt ter plaatste gestort zonder bekisting.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlUitvoeringsmethode/ter-plaatse-gestort-zonder-bekisting')
    }

