# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSoftwareLicentie(KeuzelijstField):
    """De licentievorm van de software."""
    naam = 'KlSoftwareLicentie'
    label = 'Software licentie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSoftwareLicentie'
    definition = 'De licentievorm van de software.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSoftwareLicentie'
    options = {
        'commercieel': KeuzelijstWaarde(invulwaarde='commercieel',
                                        label='commercieel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/commercieel'),
        'freeware': KeuzelijstWaarde(invulwaarde='freeware',
                                     label='freeware',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/freeware'),
        'open-source-Apache': KeuzelijstWaarde(invulwaarde='open-source-Apache',
                                               label='open source Apache',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-Apache'),
        'open-source-BSD': KeuzelijstWaarde(invulwaarde='open-source-BSD',
                                            label='open source BSD',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-BSD'),
        'open-source-GPL': KeuzelijstWaarde(invulwaarde='open-source-GPL',
                                            label='open source GPL',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/open-source-GPL'),
        'shareware': KeuzelijstWaarde(invulwaarde='shareware',
                                      label='shareware',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSoftwareLicentie/shareware')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSoftwareLicentie.get_dummy_data()

