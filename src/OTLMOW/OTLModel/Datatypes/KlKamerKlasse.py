# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKamerKlasse(KeuzelijstField):
    """De stabiliteitsklasse van de kamer."""
    naam = 'KlKamerKlasse'
    label = 'Kamer klasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKamerKlasse'
    definition = 'De stabiliteitsklasse van de kamer.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKamerKlasse'
    options = {
        'klasse-1': KeuzelijstWaarde(invulwaarde='klasse-1',
                                     label='klasse 1',
                                     definitie='klasse 1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-1'),
        'klasse-2': KeuzelijstWaarde(invulwaarde='klasse-2',
                                     label='klasse 2',
                                     definitie='klasse 2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKamerKlasse/klasse-2')
    }

