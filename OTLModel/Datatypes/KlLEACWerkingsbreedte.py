# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACWerkingsbreedte(KeuzelijstField):
    """De verschillende mogelijke werkingsbreedtes."""
    naam = 'KlLEACWerkingsbreedte'
    label = 'Werkingsbreedte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACWerkingsbreedte'
    definition = 'De verschillende mogelijke werkingsbreedtes.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACWerkingsbreedte'
    options = {
        'W1': KeuzelijstWaarde(invulwaarde='W1',
                               label='W1',
                               definitie='Wn<=0,6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W1'),
        'W2': KeuzelijstWaarde(invulwaarde='W2',
                               label='W2',
                               definitie='Wn<=0,8',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W2'),
        'W3': KeuzelijstWaarde(invulwaarde='W3',
                               label='W3',
                               definitie='Wn<=1,0',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W3'),
        'W4': KeuzelijstWaarde(invulwaarde='W4',
                               label='W4',
                               definitie='Wn<=1,3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W4'),
        'W5': KeuzelijstWaarde(invulwaarde='W5',
                               label='W5',
                               definitie='Wn<=1,7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W5'),
        'W6': KeuzelijstWaarde(invulwaarde='W6',
                               label='W6',
                               definitie='Wn<=2,1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W6'),
        'W7': KeuzelijstWaarde(invulwaarde='W7',
                               label='W7',
                               definitie='Wn<=2,5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W7'),
        'W8': KeuzelijstWaarde(invulwaarde='W8',
                               label='W8',
                               definitie='Wn<=3,5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W8')
    }

