# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGCMeetMethode(KeuzelijstField):
    """Locaties van de geluidstestproef."""
    naam = 'KlGCMeetMethode'
    label = 'Meet methode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGCMeetMethode'
    definition = 'Locaties van de geluidstestproef.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGCMeetMethode'
    options = {
        'inSitu': KeuzelijstWaarde(invulwaarde='inSitu',
                                   label='inSitu',
                                   definitie='Proef uitgevoerd op de werf',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/inSitu'),
        'labo': KeuzelijstWaarde(invulwaarde='labo',
                                 label='labo',
                                 definitie='Proef uitgevoerd in het labo',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/labo')
    }

