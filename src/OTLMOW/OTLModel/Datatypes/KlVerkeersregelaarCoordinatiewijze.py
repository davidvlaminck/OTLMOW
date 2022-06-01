# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersregelaarCoordinatiewijze(KeuzelijstField):
    """Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars."""
    naam = 'KlVerkeersregelaarCoordinatiewijze'
    label = 'Verkeersregelaar coordinatiewijze'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersregelaarCoordinatiewijze'
    definition = 'Keuzelijst met de voorkomende manieren van coordinate voor verkeersregelaars.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersregelaarCoordinatiewijze'
    options = {
        'centraal': KeuzelijstWaarde(invulwaarde='centraal',
                                     label='centraal',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/centraal'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/geen'),
        'its-app': KeuzelijstWaarde(invulwaarde='its-app',
                                    label='ITS-app',
                                    definitie='Coordinatie door ITS-app.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/its-app'),
        'klok': KeuzelijstWaarde(invulwaarde='klok',
                                 label='klok',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/klok'),
        'master': KeuzelijstWaarde(invulwaarde='master',
                                   label='master',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/master'),
        'pulsen': KeuzelijstWaarde(invulwaarde='pulsen',
                                   label='pulsen',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/pulsen'),
        'slave': KeuzelijstWaarde(invulwaarde='slave',
                                  label='slave',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersregelaarCoordinatiewijze/slave')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVerkeersregelaarCoordinatiewijze.get_dummy_data()

