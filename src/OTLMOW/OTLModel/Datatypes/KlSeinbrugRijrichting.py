# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugRijrichting(KeuzelijstField):
    """Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele)."""
    naam = 'KlSeinbrugRijrichting'
    label = 'Seinbrug rijrichting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugRijrichting'
    definition = 'Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugRijrichting'
    options = {
        'dubbele-rijrichting': KeuzelijstWaarde(invulwaarde='dubbele-rijrichting',
                                                label='dubbele rijrichting',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/dubbele-rijrichting'),
        'enkele-rijrichting': KeuzelijstWaarde(invulwaarde='enkele-rijrichting',
                                               label='enkele rijrichting',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/enkele-rijrichting')
    }

