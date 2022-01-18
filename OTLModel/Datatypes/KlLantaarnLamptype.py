# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLantaarnLamptype(KeuzelijstField):
    """Keuzelijst met LantaarnLamp types."""
    naam = 'KlLantaarnLamptype'
    label = 'Lantaarn lamptype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLantaarnLamptype'
    definition = 'Keuzelijst met LantaarnLamp types.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLantaarnLamptype'
    options = {
        'LED': KeuzelijstWaarde(invulwaarde='LED',
                                label='LED',
                                definitie='Led lamp.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/LED'),
        'gasontlading': KeuzelijstWaarde(invulwaarde='gasontlading',
                                         label='gasontlading',
                                         definitie='Lamp op basis van gas.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gasontlading'),
        'gloeilamp': KeuzelijstWaarde(invulwaarde='gloeilamp',
                                      label='gloeilamp',
                                      definitie='Gloeilamp.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/gloeilamp'),
        'halogeen': KeuzelijstWaarde(invulwaarde='halogeen',
                                     label='halogeen',
                                     definitie='Halogeenlamp.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLantaarnLamptype/halogeen')
    }

