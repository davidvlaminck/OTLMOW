# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSchanskorfVorm(KeuzelijstField):
    """Vormen van schanskorven."""
    naam = 'KlSchanskorfVorm'
    label = 'Schanskorf vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSchanskorfVorm'
    definition = 'Vormen van schanskorven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSchanskorfVorm'
    options = {
        'in-blokvorm': KeuzelijstWaarde(invulwaarde='in-blokvorm',
                                        label='in blokvorm',
                                        definitie='in blokvorm',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-blokvorm'),
        'in-matrasvorm': KeuzelijstWaarde(invulwaarde='in-matrasvorm',
                                          label='in matrasvorm',
                                          definitie='in matrasvorm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSchanskorfVorm/in-matrasvorm')
    }

