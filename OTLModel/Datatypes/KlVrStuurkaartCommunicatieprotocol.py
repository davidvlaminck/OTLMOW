# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVrStuurkaartCommunicatieprotocol(KeuzelijstField):
    """Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten."""
    naam = 'KlVrStuurkaartCommunicatieprotocol'
    label = 'VRI-communicatieprotocol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVrStuurkaartCommunicatieprotocol'
    definition = 'Keuzelist met de voorkomende communicatieprotocollen voor VRIstuurkaarten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVrStuurkaartCommunicatieprotocol'
    options = {
        'canto': KeuzelijstWaarde(invulwaarde='canto',
                                  label='canto',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/canto'),
        'gecombineerd': KeuzelijstWaarde(invulwaarde='gecombineerd',
                                         label='gecombineerd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/gecombineerd'),
        'ocit': KeuzelijstWaarde(invulwaarde='ocit',
                                 label='ocit',
                                 definitie='nog in te vullen',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVrStuurkaartCommunicatieprotocol/ocit')
    }

