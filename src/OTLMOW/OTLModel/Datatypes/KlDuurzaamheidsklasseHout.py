# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDuurzaamheidsklasseHout(KeuzelijstField):
    """De resistentie van het kernhout tegen ongunstige omstandigheden."""
    naam = 'KlDuurzaamheidsklasseHout'
    label = 'Duurzaamheidsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlDuurzaamheidsklasseHout'
    definition = 'De resistentie van het kernhout tegen ongunstige omstandigheden.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDuurzaamheidsklasseHout'
    options = {
        'klasse-i': KeuzelijstWaarde(invulwaarde='klasse-i',
                                     label='Klasse I',
                                     status='ingebruik',
                                     definitie='Zeer duurzaam.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-i'),
        'klasse-ii': KeuzelijstWaarde(invulwaarde='klasse-ii',
                                      label='Klasse II',
                                      status='ingebruik',
                                      definitie='Duurzaam.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-ii'),
        'klasse-iii': KeuzelijstWaarde(invulwaarde='klasse-iii',
                                       label='Klasse III',
                                       status='ingebruik',
                                       definitie='Matig duurzaam.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-iii'),
        'klasse-iv': KeuzelijstWaarde(invulwaarde='klasse-iv',
                                      label='Klasse IV',
                                      status='ingebruik',
                                      definitie='Weinig duurzaam.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-iv'),
        'klasse-v': KeuzelijstWaarde(invulwaarde='klasse-v',
                                     label='Klasse V',
                                     status='ingebruik',
                                     definitie='Niet duurzaam.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDuurzaamheidsklasseHout/klasse-v')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

