# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignaalkabelType(KeuzelijstField):
    """Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270."""
    naam = 'KlSignaalkabelType'
    label = 'Signalisatiekabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignaalkabelType'
    definition = 'Lijst met types voor signalisatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignaalkabelType'
    options = {
        'koperkabel': KeuzelijstWaarde(invulwaarde='koperkabel',
                                       label='koperkabel',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/koperkabel'),
        'profibuskabel': KeuzelijstWaarde(invulwaarde='profibuskabel',
                                          label='profibuskabel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/profibuskabel'),
        'svavb-f2': KeuzelijstWaarde(invulwaarde='svavb-f2',
                                     label='SVAVB-F2',
                                     definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svavb-f2'),
        'svv-f2': KeuzelijstWaarde(invulwaarde='svv-f2',
                                   label='SVV-F2',
                                   definitie='Niet-gewapende signaalkabel voor binnen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/svv-f2'),
        'sxag-f2': KeuzelijstWaarde(invulwaarde='sxag-f2',
                                    label='SXAG-F2',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxag-f2'),
        'sxavb': KeuzelijstWaarde(invulwaarde='sxavb',
                                  label='SXAVB',
                                  definitie='Gewapende signaalkabel voor ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignaalkabelType/sxavb')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSignaalkabelType.get_dummy_data()

