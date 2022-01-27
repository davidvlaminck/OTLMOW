# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOnderbouwType(KeuzelijstField):
    """Types van onderbouw."""
    naam = 'KlOnderbouwType'
    label = 'Onderbouw type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOnderbouwType'
    definition = 'Types van onderbouw.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOnderbouwType'
    options = {
        'bodemsubstraat': KeuzelijstWaarde(invulwaarde='bodemsubstraat',
                                           label='bodemsubstraat',
                                           definitie='Fundering van bodemsubstraat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat'),
        'bodemsubstraat-met-steenslag': KeuzelijstWaarde(invulwaarde='bodemsubstraat-met-steenslag',
                                                         label='bodemsubstraat met steenslag',
                                                         definitie='Fundering van bodemsubstraat met steenslag',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat-met-steenslag'),
        'bodemsubstraat-met-zand': KeuzelijstWaarde(invulwaarde='bodemsubstraat-met-zand',
                                                    label='bodemsubstraat met zand',
                                                    definitie='Fundering van bodemsubstraat met zand',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/bodemsubstraat-met-zand'),
        'draineerzand': KeuzelijstWaarde(invulwaarde='draineerzand',
                                         label='draineerzand',
                                         definitie='Fundering van draineerzand.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/draineerzand'),
        'drainerend-schraal-beton': KeuzelijstWaarde(invulwaarde='drainerend-schraal-beton',
                                                     label='drainerend schraal beton',
                                                     definitie='Fundering van drainerend schraal beton',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/drainerend-schraal-beton'),
        'drainerend-zandcement': KeuzelijstWaarde(invulwaarde='drainerend-zandcement',
                                                  label='drainerend zandcement',
                                                  definitie='Fundering van drainerend zandcement.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/drainerend-zandcement'),
        'geschikt-gemaakt-aanvullingsmateriaal': KeuzelijstWaarde(invulwaarde='geschikt-gemaakt-aanvullingsmateriaal',
                                                                  label='geschikt gemaakt aanvullingsmateriaal',
                                                                  definitie='Fundering van geschikt gemaakt aanvullingsmateriaal',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/geschikt-gemaakt-aanvullingsmateriaal'),
        'granulaatcement': KeuzelijstWaarde(invulwaarde='granulaatcement',
                                            label='granulaatcement',
                                            definitie='granulaatcement',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatcement'),
        'granulaatmengsel-0-4': KeuzelijstWaarde(invulwaarde='granulaatmengsel-0-4',
                                                 label='granulaatmengsel 0-4',
                                                 definitie='Fundering van granulaatmengsel 0/4',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatmengsel-0-4'),
        'granulaatmengsel-0-6.3': KeuzelijstWaarde(invulwaarde='granulaatmengsel-0-6.3',
                                                   label='granulaatmengsel 0-6.3',
                                                   definitie='Fudnering van granulaatmengsel 0/6.3',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/granulaatmengsel-0-6.3'),
        'met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IA': KeuzelijstWaarde(invulwaarde='met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IA',
                                                                                                       label='met toevoegsel behandelde steenslag met continue korrelverdeling - type IA',
                                                                                                       definitie='Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IA',
                                                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IA'),
        'met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IB': KeuzelijstWaarde(invulwaarde='met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IB',
                                                                                                       label='met toevoegsel behandelde steenslag met continue korrelverdeling - type IB',
                                                                                                       definitie='Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IB',
                                                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IB'),
        'met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIA': KeuzelijstWaarde(invulwaarde='met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIA',
                                                                                                        label='met toevoegsel behandelde steenslag met continue korrelverdeling - type IIA',
                                                                                                        definitie='Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IIA',
                                                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIA'),
        'met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIB': KeuzelijstWaarde(invulwaarde='met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIB',
                                                                                                        label='met toevoegsel behandelde steenslag met continue korrelverdeling - type IIB',
                                                                                                        definitie='Fundering van met toevoegsel behandelde steenslag met continue korrelverdeling - type IIB',
                                                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/met-toevoegsel-behandelde-steenslag-met-continue-korrelverdeling---type-IIB'),
        'mortel': KeuzelijstWaarde(invulwaarde='mortel',
                                   label='mortel',
                                   definitie='Fundering van mortel',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/mortel'),
        'onderfundering-type-I': KeuzelijstWaarde(invulwaarde='onderfundering-type-I',
                                                  label='onderfundering type I',
                                                  definitie='onderfundering type I',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-I'),
        'onderfundering-type-II': KeuzelijstWaarde(invulwaarde='onderfundering-type-II',
                                                   label='onderfundering type II',
                                                   definitie='onderfundering type II',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-II'),
        'onderfundering-type-III': KeuzelijstWaarde(invulwaarde='onderfundering-type-III',
                                                    label='onderfundering type III',
                                                    definitie='onderfundering type III',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/onderfundering-type-III'),
        'schraal-asfalt': KeuzelijstWaarde(invulwaarde='schraal-asfalt',
                                           label='schraal asfalt',
                                           definitie='Fundering van schraal asfalt',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraal-asfalt'),
        'schraal-beton': KeuzelijstWaarde(invulwaarde='schraal-beton',
                                          label='schraal beton',
                                          definitie='Fundering van schraal beton.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraal-beton'),
        'schraalbeton-met-stut': KeuzelijstWaarde(invulwaarde='schraalbeton-met-stut',
                                                  label='schraalbeton met stut',
                                                  definitie='Fundering van schraalbeton met stut',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/schraalbeton-met-stut'),
        'skeletbodems': KeuzelijstWaarde(invulwaarde='skeletbodems',
                                         label='skeletbodems',
                                         definitie='Fundering van skeletbodems.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/skeletbodems'),
        'stabiliseren-van-de-bestaande-verharding-met-cement-(recycling-in-situ)': KeuzelijstWaarde(invulwaarde='stabiliseren-van-de-bestaande-verharding-met-cement-(recycling-in-situ)',
                                                                                                    label='stabiliseren van de bestaande verharding met cement (recycling in situ)',
                                                                                                    definitie='Fundering door het stabiliseren van de bestaande verharding met cement (recycling in situ)',
                                                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/stabiliseren-van-de-bestaande-verharding-met-cement-(recycling-in-situ)'),
        'steenslag-2-4': KeuzelijstWaarde(invulwaarde='steenslag-2-4',
                                          label='steenslag 2-4',
                                          definitie='Fundering van steenslag 2/4',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-2-4'),
        'steenslag-2-6.3': KeuzelijstWaarde(invulwaarde='steenslag-2-6.3',
                                            label='steenslag 2-6.3',
                                            definitie='Fundering van steenslag 2/6.3',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-2-6.3'),
        'steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-I': KeuzelijstWaarde(invulwaarde='steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-I',
                                                                                              label='steenslag met continue korrelverdeling zonder toevoegsel - type I',
                                                                                              definitie='Fundering van steenslag met continue korrelverdeling zonder toevoegsel - type I',
                                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-I'),
        'steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-II': KeuzelijstWaarde(invulwaarde='steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-II',
                                                                                               label='steenslag met continue korrelverdeling zonder toevoegsel - type II',
                                                                                               definitie='Fundering van steenslag met continue korrelverdeling zonder toevoegsel - type II',
                                                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-continue-korrelverdeling-zonder-toevoegsel---type-II'),
        'steenslag-met-niet-continue-korrelverdeling': KeuzelijstWaarde(invulwaarde='steenslag-met-niet-continue-korrelverdeling',
                                                                        label='steenslag met niet-continue korrelverdeling',
                                                                        definitie='Fundering van steenslagfundering met niet-continue korrelverdeling',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-met-niet-continue-korrelverdeling'),
        'steenslag-of-rolgrind': KeuzelijstWaarde(invulwaarde='steenslag-of-rolgrind',
                                                  label='steenslag of rolgrind',
                                                  definitie='Fundering van steenslag of rolgrind.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/steenslag-of-rolgrind'),
        'teerhoudend-asfaltgranulaatcement': KeuzelijstWaarde(invulwaarde='teerhoudend-asfaltgranulaatcement',
                                                              label='teerhoudend asfaltgranulaatcement',
                                                              definitie='Fundering in teerhoudend asfaltgranulaatcement',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/teerhoudend-asfaltgranulaatcement'),
        'ternair-mengsel': KeuzelijstWaarde(invulwaarde='ternair-mengsel',
                                            label='ternair mengsel',
                                            definitie='Fundering van ternair mengsel',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/ternair-mengsel'),
        'tijdelijke-steenslag-miv-verwijdering': KeuzelijstWaarde(invulwaarde='tijdelijke-steenslag-miv-verwijdering',
                                                                  label='tijdelijke steenslag miv verwijdering',
                                                                  definitie='Fundering van tijdelijke steenslag miv verwijdering',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/tijdelijke-steenslag-miv-verwijdering'),
        'vliegas-cementmengsel': KeuzelijstWaarde(invulwaarde='vliegas-cementmengsel',
                                                  label='vliegas cementmengsel',
                                                  definitie='Fundering van vliesgas-cementmengsel.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/vliegas-cementmengsel'),
        'vliegas-kalkmengsel': KeuzelijstWaarde(invulwaarde='vliegas-kalkmengsel',
                                                label='vliegas kalkmengsel',
                                                definitie='Fundering van vliesgas-kalkmengsel',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/vliegas-kalkmengsel'),
        'walsbeton': KeuzelijstWaarde(invulwaarde='walsbeton',
                                      label='walsbeton',
                                      definitie='Fundering van walsbeton.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/walsbeton'),
        'waterdoorlatende-steenslagfundering': KeuzelijstWaarde(invulwaarde='waterdoorlatende-steenslagfundering',
                                                                label='waterdoorlatende steenslagfundering',
                                                                definitie='Fundering van waterdoorlatende steenslagfundering',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/waterdoorlatende-steenslagfundering'),
        'wortelruimte---bomengranulaat': KeuzelijstWaarde(invulwaarde='wortelruimte---bomengranulaat',
                                                          label='wortelruimte - bomengranulaat',
                                                          definitie='Fundering wortelruimte - bomengranulaat',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---bomengranulaat'),
        'wortelruimte---bomenzand': KeuzelijstWaarde(invulwaarde='wortelruimte---bomenzand',
                                                     label='wortelruimte - bomenzand',
                                                     definitie='Fundering wortelruimte - bomenzand',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---bomenzand'),
        'wortelruimte---groeiplaatsconstructie': KeuzelijstWaarde(invulwaarde='wortelruimte---groeiplaatsconstructie',
                                                                  label='wortelruimte - groeiplaatsconstructie',
                                                                  definitie='Fundering wortelruimte - groeiplaatsconstructie',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/wortelruimte---groeiplaatsconstructie'),
        'zand': KeuzelijstWaarde(invulwaarde='zand',
                                 label='zand',
                                 definitie='Fundering van zand',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zand'),
        'zandcement': KeuzelijstWaarde(invulwaarde='zandcement',
                                       label='zandcement',
                                       definitie='Fundering van zandcement',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zandcement'),
        'zandcement-met-stut': KeuzelijstWaarde(invulwaarde='zandcement-met-stut',
                                                label='zandcement met stut',
                                                definitie='Fundering van zandcement met stut',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnderbouwType/zandcement-met-stut')
    }

