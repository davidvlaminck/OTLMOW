# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOnderwaterkruisingAanlegWijze(KeuzelijstField):
    """Lijst met mogelijke manieren van aanleg waarmee onderwaterkruisingen kunnen gerealiseerd worden."""
    naam = 'KlOnderwaterkruisingAanlegWijze'
    label = 'Onderwaterkruising aanleg wijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOnderwaterkruisingAanlegWijze'
    definition = 'Lijst met mogelijke manieren van aanleg waarmee onderwaterkruisingen kunnen gerealiseerd worden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOnderwaterkruisingAanlegWijze'
    options = {
        'ingegoten-in-sluis': KeuzelijstWaarde(invulwaarde='ingegoten-in-sluis',
                                               label='ingegoten in sluis',
                                               status='ingebruik',
                                               definitie='Buizen in een sleuf aangestort met beton, in de deurnis, drempel of sluisvloer.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderwaterkruisingAanlegWijze/ingegoten-in-sluis'),
        'ingegraven': KeuzelijstWaarde(invulwaarde='ingegraven',
                                       label='ingegraven',
                                       status='ingebruik',
                                       definitie='Buizen in een sleuf in de bodem van een waterweg die vervolgens terug aangestort wordt met specie.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderwaterkruisingAanlegWijze/ingegraven'),
        'met-zandzakken-vastgelegd': KeuzelijstWaarde(invulwaarde='met-zandzakken-vastgelegd',
                                                      label='met zandzakken vastgelegd',
                                                      status='ingebruik',
                                                      definitie='Buizen in of op de bodem van een waterweg die afgedekt worden met gewicht in de vorm van zandzakken, grote metalen stukken of arduinen blokken.',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderwaterkruisingAanlegWijze/met-zandzakken-vastgelegd')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

