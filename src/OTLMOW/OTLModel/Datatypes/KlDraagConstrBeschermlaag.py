# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDraagConstrBeschermlaag(KeuzelijstField):
    """De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming."""
    naam = 'KlDraagConstrBeschermlaag'
    label = 'Draagconstructie beschermlaag'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagConstrBeschermlaag'
    definition = 'De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBeschermlaag'
    options = {
        'gecoat': KeuzelijstWaarde(invulwaarde='gecoat',
                                   label='gecoat',
                                   definitie='Een mengsel van stoffen aangebracht om roest te voorkomen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gecoat'),
        'gegalvaniseerd': KeuzelijstWaarde(invulwaarde='gegalvaniseerd',
                                           label='gegalvaniseerd',
                                           definitie='Een laag zink aangebracht om roest te voorkomen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gegalvaniseerd'),
        'geschilderd': KeuzelijstWaarde(invulwaarde='geschilderd',
                                        label='geschilderd',
                                        definitie='Een laag verf aangebracht om roest te voorkomen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/geschilderd')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDraagConstrBeschermlaag.get_dummy_data()

