# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeegsensorMerk(KeuzelijstField):
    """Het merk van de weegsensor."""
    naam = 'KlWeegsensorMerk'
    label = 'Weegsensor merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorMerk'
    definition = 'Het merk van de weegsensor.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorMerk'
    options = {
        'Kistler': KeuzelijstWaarde(invulwaarde='Kistler',
                                    label='Kistler',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorMerk/Kistler')
    }

