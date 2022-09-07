# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSterkteklasseHout(KeuzelijstField):
    """De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning."""
    naam = 'KlSterkteklasseHout'
    label = 'Sterkteklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSterkteklasseHout'
    definition = 'De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSterkteklasseHout'
    options = {
        'c14': KeuzelijstWaarde(invulwaarde='c14',
                                label='C14',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 14 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c14'),
        'c16': KeuzelijstWaarde(invulwaarde='c16',
                                label='C16',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 16 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c16'),
        'c18': KeuzelijstWaarde(invulwaarde='c18',
                                label='C18',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 18 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c18'),
        'c20': KeuzelijstWaarde(invulwaarde='c20',
                                label='C20',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 20 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c20'),
        'c22': KeuzelijstWaarde(invulwaarde='c22',
                                label='C22',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 22 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c22'),
        'c24': KeuzelijstWaarde(invulwaarde='c24',
                                label='C24',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 24 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c24'),
        'c27': KeuzelijstWaarde(invulwaarde='c27',
                                label='C27',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 27 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c27'),
        'c30': KeuzelijstWaarde(invulwaarde='c30',
                                label='C30',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 30 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c30'),
        'c35': KeuzelijstWaarde(invulwaarde='c35',
                                label='C35',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 35 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c35'),
        'c40': KeuzelijstWaarde(invulwaarde='c40',
                                label='C40',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 40 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c40'),
        'c45': KeuzelijstWaarde(invulwaarde='c45',
                                label='C45',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 45 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c45'),
        'c50': KeuzelijstWaarde(invulwaarde='c50',
                                label='C50',
                                status='ingebruik',
                                definitie='C staat voor naaldhout. 50 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/c50'),
        'd30': KeuzelijstWaarde(invulwaarde='d30',
                                label='D30',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 30 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d30'),
        'd35': KeuzelijstWaarde(invulwaarde='d35',
                                label='D35',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 35 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d35'),
        'd40': KeuzelijstWaarde(invulwaarde='d40',
                                label='D40',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 40 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d40'),
        'd50': KeuzelijstWaarde(invulwaarde='d50',
                                label='D50',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 50 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d50'),
        'd60': KeuzelijstWaarde(invulwaarde='d60',
                                label='D60',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 60 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d60'),
        'd70': KeuzelijstWaarde(invulwaarde='d70',
                                label='D70',
                                status='ingebruik',
                                definitie='D staat voor loofhout. 70 N/mm² (megaPascal) drukt de buigsterkte uit evenwijdig aan de vezel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSterkteklasseHout/d70')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

