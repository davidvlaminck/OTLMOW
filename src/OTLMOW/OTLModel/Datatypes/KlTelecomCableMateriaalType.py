# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecomCableMateriaalType(KeuzelijstField):
    """Codelijst met waardes voor het type materiaal van een telecomkabel."""
    naam = 'KlTelecomCableMateriaalType'
    label = 'Datakabel materiaal'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlTelecomCableMateriaalType'
    definition = 'Codelijst met waardes voor het type materiaal van een telecomkabel.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecomCableMateriaalType'
    options = {
        'coaxial': KeuzelijstWaarde(invulwaarde='coaxial',
                                    label='coaxial',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/coaxial'),
        'opticalfiber': KeuzelijstWaarde(invulwaarde='opticalfiber',
                                         label='opticalFiber',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/opticalfiber'),
        'other': KeuzelijstWaarde(invulwaarde='other',
                                  label='other',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/other'),
        'twistedpair': KeuzelijstWaarde(invulwaarde='twistedpair',
                                        label='twistedPair',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomCableMateriaalType/twistedpair')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTelecomCableMateriaalType.get_dummy_data()

