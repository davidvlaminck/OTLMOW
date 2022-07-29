# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACWerkingsbreedte(KeuzelijstField):
    """De verschillende mogelijke werkingsbreedtes."""
    naam = 'KlLEACWerkingsbreedte'
    label = 'Werkingsbreedte'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACWerkingsbreedte'
    definition = 'De verschillende mogelijke werkingsbreedtes.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACWerkingsbreedte'
    options = {
        'W1': KeuzelijstWaarde(invulwaarde='W1',
                               label='W1',
                               status='ingebruik',
                               definitie='Wn<=0,6',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W1'),
        'W2': KeuzelijstWaarde(invulwaarde='W2',
                               label='W2',
                               status='ingebruik',
                               definitie='Wn<=0,8',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W2'),
        'W3': KeuzelijstWaarde(invulwaarde='W3',
                               label='W3',
                               status='ingebruik',
                               definitie='Wn<=1,0',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W3'),
        'W4': KeuzelijstWaarde(invulwaarde='W4',
                               label='W4',
                               status='ingebruik',
                               definitie='Wn<=1,3',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W4'),
        'W5': KeuzelijstWaarde(invulwaarde='W5',
                               label='W5',
                               status='ingebruik',
                               definitie='Wn<=1,7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W5'),
        'W6': KeuzelijstWaarde(invulwaarde='W6',
                               label='W6',
                               status='ingebruik',
                               definitie='Wn<=2,1',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W6'),
        'W7': KeuzelijstWaarde(invulwaarde='W7',
                               label='W7',
                               status='ingebruik',
                               definitie='Wn<=2,5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W7'),
        'W8': KeuzelijstWaarde(invulwaarde='W8',
                               label='W8',
                               status='ingebruik',
                               definitie='Wn<=3,5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACWerkingsbreedte/W8')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

