# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordZ30Merk(KeuzelijstField):
    """Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""
    naam = 'KlDynBordZ30Merk'
    label = 'Z30 merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordZ30Merk'
    definition = 'Keuzelijst met de gangbare merken van dynamische zone 30 borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordZ30Merk'
    options = {
        'Futurit': KeuzelijstWaarde(invulwaarde='Futurit',
                                    label='Futurit',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Futurit'),
        'Q-lite': KeuzelijstWaarde(invulwaarde='Q-lite',
                                   label='Q-lite',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Merk/Q-lite')
    }

