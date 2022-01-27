# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelnettoegangNetwerksoort(KeuzelijstField):
    """Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt."""
    naam = 'KlKabelnettoegangNetwerksoort'
    label = 'Kabelnet toegang netwerksoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelnettoegangNetwerksoort'
    definition = 'Lijst van netwerktypes die bereikbaar is via het kabelnet toegangspunt.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelnettoegangNetwerksoort'
    options = {
        'Cu': KeuzelijstWaarde(invulwaarde='Cu',
                               label='Cu',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/Cu'),
        'FO': KeuzelijstWaarde(invulwaarde='FO',
                               label='FO',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelnettoegangNetwerksoort/FO')
    }

