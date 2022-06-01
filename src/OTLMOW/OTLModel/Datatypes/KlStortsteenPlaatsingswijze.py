# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenPlaatsingswijze(KeuzelijstField):
    """De manier waarop de stenen worden geplaatst."""
    naam = 'KlStortsteenPlaatsingswijze'
    label = 'Plaatsingswijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenPlaatsingswijze'
    definition = 'De manier waarop de stenen worden geplaatst.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenPlaatsingswijze'
    options = {
        'gestapeld': KeuzelijstWaarde(invulwaarde='gestapeld',
                                      label='gestapeld',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gestapeld'),
        'gewone-bestorting-met-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-met-fixatie-colloïdaal-beton',
                                                                           label='gewone bestorting met fixatie colloïdaal beton',
                                                                           definitie='gewone bestorting met fixatie colloïdaal beton',
                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-met-fixatie-colloïdaal-beton'),
        'gewone-bestorting-zonder-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='gewone-bestorting-zonder-fixatie-colloïdaal-beton',
                                                                              label='gewone bestorting zonder fixatie colloïdaal beton',
                                                                              definitie='gewone bestorting zonder fixatie colloïdaal beton',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/gewone-bestorting-zonder-fixatie-colloïdaal-beton'),
        'stroomkuilenprofiel-met-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-met-fixatie-colloïdaal-beton',
                                                                             label='stroomkuilenprofiel met fixatie colloïdaal beton',
                                                                             definitie='stroomkuilenprofiel met fixatie colloïdaal beton',
                                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-met-fixatie-colloïdaal-beton'),
        'stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton': KeuzelijstWaarde(invulwaarde='stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton',
                                                                                label='stroomkuilenprofiel zonder fixatie colloïdaal beton',
                                                                                definitie='stroomkuilenprofiel zonder fixatie colloïdaal beton',
                                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenPlaatsingswijze/stroomkuilenprofiel-zonder-fixatie-colloïdaal-beton')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlStortsteenPlaatsingswijze.get_dummy_data()

