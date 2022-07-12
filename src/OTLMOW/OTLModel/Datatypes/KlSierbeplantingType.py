# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplantingType(KeuzelijstField):
    """Verschillende types van sierbeplanting."""
    naam = 'KlSierbeplantingType'
    label = 'Sierbeplanting type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplantingType'
    definition = 'Verschillende types van sierbeplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplantingType'
    options = {
        'bodembedekkers': KeuzelijstWaarde(invulwaarde='bodembedekkers',
                                           label='bodembedekkers',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Aangelegd begroeiingstype, doorgaans met vaste planten, die bedoeld is om snel de bodem af te dekken.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bodembedekkers'),
        'bol-en-knolgewassen': KeuzelijstWaarde(invulwaarde='bol-en-knolgewassen',
                                                label='bol- en knolgewassen',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='Bol- en knolgewassen beschikken over boven- of ondergrondse delen waarin voedsel voor ‘barre’ tijden kan worden opgeslagen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bol-en-knolgewassen'),
        'siergrassen': KeuzelijstWaarde(invulwaarde='siergrassen',
                                        label='siergrassen',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Grasachtige planten, doorgaans vaste planten, met een decoratieve waarde. Niet geplant als gazon',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/siergrassen'),
        'vaste-planten': KeuzelijstWaarde(invulwaarde='vaste-planten',
                                          label='vaste planten',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Begroeiingstype met planten die een kruidachtige stengel hebben en overblijvend zijn. Dus niet de eenjarige en tweejarige kruidachtige soorten.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/vaste-planten')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlSierbeplantingType.get_dummy_data()

