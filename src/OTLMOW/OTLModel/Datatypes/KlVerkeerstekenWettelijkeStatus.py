# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeerstekenWettelijkeStatus(KeuzelijstField):
    """Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven."""
    naam = 'KlVerkeerstekenWettelijkeStatus'
    label = 'VerkeerstekenWettelijkeStatus'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeerstekenWettelijkeStatus'
    definition = 'Keuzelijst met waarden die de wettelijke status van een verkeersteken aangeven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeerstekenWettelijkeStatus'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

