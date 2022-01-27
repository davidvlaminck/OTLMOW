# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerSierbeplanting(KeuzelijstField):
    """Verschillende mogelijke beheeropties bij sierbeplanting."""
    naam = 'KlBeheerSierbeplanting'
    label = 'Beheer sierbeplanting'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerSierbeplanting'
    definition = 'Verschillende mogelijke beheeropties bij sierbeplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerSierbeplanting'
    options = {
        'hakken': KeuzelijstWaarde(invulwaarde='hakken',
                                   label='hakken',
                                   definitie='Hakken van de grond tussen sierbeplantingen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/hakken'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       definitie='Er wordt geen beheer uitgevoerd.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/niets-doen'),
        'opschikken-knippen-dood-materiaal': KeuzelijstWaarde(invulwaarde='opschikken-knippen-dood-materiaal',
                                                              label='opschikken-knippen dood materiaal',
                                                              definitie='Opschikken/knippen van dood materiaal.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/opschikken-knippen-dood-materiaal'),
        'scheren': KeuzelijstWaarde(invulwaarde='scheren',
                                    label='scheren',
                                    definitie='Het vlakvormig gelijkmatig kort afsnijden van takken van hagen, heesters en houtkanten.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/scheren'),
        'snoeien': KeuzelijstWaarde(invulwaarde='snoeien',
                                    label='snoeien',
                                    definitie='Het inkorten of wegnemen van stengels met snoeischaar.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/snoeien'),
        'wieden': KeuzelijstWaarde(invulwaarde='wieden',
                                   label='wieden',
                                   definitie='Het wieden van de grond tussen sierbeplanting. Dit is het verwijderen van onkruid.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/wieden')
    }

