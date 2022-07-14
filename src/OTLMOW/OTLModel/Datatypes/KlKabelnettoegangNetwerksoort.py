# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelnettoegangNetwerksoort(KeuzelijstField):
    """Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt."""
    naam = 'KlKabelnettoegangNetwerksoort'
    label = 'Kabelnet toegang netwerksoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelnettoegangNetwerksoort'
    definition = 'Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelnettoegangNetwerksoort'
    options = {
        'Cu': KeuzelijstWaarde(invulwaarde='Cu',
                               label='Cu',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/Cu'),
        'FO': KeuzelijstWaarde(invulwaarde='FO',
                               label='FO',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/FO')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

