# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermType(KeuzelijstField):
    """Types van wegberm die de plaats ten opzichte van de weg aangeven."""
    naam = 'KlWegbermType'
    label = 'Wegberm type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermType'
    definition = 'Types van wegberm die de plaats ten opzichte van de weg aangeven.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermType'
    options = {
        'buitenberm': KeuzelijstWaarde(invulwaarde='buitenberm',
                                       label='buitenberm',
                                       definitie='Wegberm tussen de grens van het wegplatform en de buitengrens van de verharde zijstrook of van de rijbaan, als er geen verharde zijstrook is.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/buitenberm'),
        'middenberm': KeuzelijstWaarde(invulwaarde='middenberm',
                                       label='middenberm',
                                       definitie='Wegberm tussen de middelste rijbanen van een weg met een even aantal rijbanen.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/middenberm'),
        'tussenberm': KeuzelijstWaarde(invulwaarde='tussenberm',
                                       label='tussenberm',
                                       definitie='Wegberm tussen twee rijbanen van een weg met meer dan één rijbaan, de middenberm uitgezonderd.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermType/tussenberm')
    }

