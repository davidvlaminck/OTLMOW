# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcoductType(KeuzelijstField):
    """Types van ecoduct."""
    naam = 'KlEcoEcoductType'
    label = 'Ecoduct type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcoductType'
    definition = 'Types van ecoduct.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcoductType'
    options = {
        'bermbrug': KeuzelijstWaarde(invulwaarde='bermbrug',
                                     label='bermbrug',
                                     definitie='Een bestaande, vaak smalle brug met beperkt verkeer waarop de natuur via groene bermen doorloopt.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/bermbrug'),
        'ecocreaduct': KeuzelijstWaarde(invulwaarde='ecocreaduct',
                                        label='ecocreaduct',
                                        definitie='Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met zachte recreatie (fietsers, wandelaars, ruiters).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecocreaduct'),
        'ecoveloduct': KeuzelijstWaarde(invulwaarde='ecoveloduct',
                                        label='ecoveloduct',
                                        definitie='Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met een fietspad.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecoveloduct')
    }

