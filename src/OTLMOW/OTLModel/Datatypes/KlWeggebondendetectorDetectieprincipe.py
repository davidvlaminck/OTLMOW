# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWeggebondendetectorDetectieprincipe(KeuzelijstField):
    """Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""
    naam = 'KlWeggebondendetectorDetectieprincipe'
    label = 'Weggebondendetector detectieprincipe'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeggebondendetectorDetectieprincipe'
    definition = 'Keuzelijst met de verschillende gangbare manieren waarop een weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeggebondendetectorDetectieprincipe'
    options = {
        'doppler': KeuzelijstWaarde(invulwaarde='doppler',
                                    label='doppler',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/doppler'),
        'inductief': KeuzelijstWaarde(invulwaarde='inductief',
                                      label='inductief',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/inductief'),
        'infrarood': KeuzelijstWaarde(invulwaarde='infrarood',
                                      label='infrarood',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood'),
        'infrarood+inductief': KeuzelijstWaarde(invulwaarde='infrarood+inductief',
                                                label='infrarood+inductief',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeggebondendetectorDetectieprincipe/infrarood+inductief')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWeggebondendetectorDetectieprincipe.get_dummy_data()

