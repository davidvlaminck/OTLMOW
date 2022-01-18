# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlHelling(KeuzelijstField):
    """Kwarten voor het bepalen van de hellingsgraad."""
    naam = 'KlHelling'
    label = 'Helling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHelling'
    definition = 'Kwarten voor het bepalen van de hellingsgraad.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHelling'
    options = {
        '10-4': KeuzelijstWaarde(invulwaarde='10-4',
                                 label='10-4',
                                 definitie='10-4',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/10-4'),
        '12-4': KeuzelijstWaarde(invulwaarde='12-4',
                                 label='12-4',
                                 definitie='12-4',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/12-4'),
        '14-4': KeuzelijstWaarde(invulwaarde='14-4',
                                 label='14-4',
                                 definitie='14-4',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/14-4'),
        '16-4': KeuzelijstWaarde(invulwaarde='16-4',
                                 label='16-4',
                                 definitie='16-4',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/16-4'),
        '18-4': KeuzelijstWaarde(invulwaarde='18-4',
                                 label='18-4',
                                 definitie='18-4',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/18-4'),
        '4-4': KeuzelijstWaarde(invulwaarde='4-4',
                                label='4-4',
                                definitie='4-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/4-4'),
        '6-4': KeuzelijstWaarde(invulwaarde='6-4',
                                label='6-4',
                                definitie='6-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/6-4'),
        '8-4': KeuzelijstWaarde(invulwaarde='8-4',
                                label='8-4',
                                definitie='8-4',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHelling/8-4')
    }

