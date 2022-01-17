# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                           definitie='Aangelegd begroeiingstype, doorgaans met vaste planten, die bedoeld is om snel de bodem af te dekken.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bodembedekkers'),
        'bol-en-knolgewassen': KeuzelijstWaarde(invulwaarde='bol-en-knolgewassen',
                                                label='bol- en knolgewassen',
                                                definitie='Bol- en knolgewassen beschikken over boven- of ondergrondse delen waarin voedsel voor ‘barre’ tijden kan worden opgeslagen.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/bol-en-knolgewassen'),
        'siergrassen': KeuzelijstWaarde(invulwaarde='siergrassen',
                                        label='siergrassen',
                                        definitie='Grasachtige planten, doorgaans vaste planten, met een decoratieve waarde. Niet geplant als gazon',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/siergrassen'),
        'vaste-planten': KeuzelijstWaarde(invulwaarde='vaste-planten',
                                          label='vaste planten',
                                          definitie='Begroeiingstype met planten die een kruidachtige stengel hebben en overblijvend zijn. Dus niet de eenjarige en tweejarige kruidachtige soorten.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplantingType/vaste-planten')
    }

