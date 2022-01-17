# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendeKokerFolieType(KeuzelijstField):
    """Keuzeijst voor het bepalen van folietype van de retroreflecterende koker."""
    naam = 'KlRetroreflecterendeKokerFolieType'
    label = 'Retroreflecterende koker folie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendeKokerFolieType'
    definition = 'Keuzeijst voor het bepalen van folietype van de retroreflecterende koker.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendeKokerFolieType'
    options = {
        'type-2': KeuzelijstWaarde(invulwaarde='type-2',
                                   label='type 2',
                                   definitie='Keuze folie type 2 (geel) als folietype van de retroreflecterende koker',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-2'),
        'type-3': KeuzelijstWaarde(invulwaarde='type-3',
                                   label='type 3',
                                   definitie='Keuze folie type 3 als folietype (geel - fluorescerend) van de retroreflecterende koker',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-3')
    }

