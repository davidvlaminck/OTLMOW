# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSignalisatieReferentiepuntType(KeuzelijstField):
    """Een keuzelijst om het referentiepunt type te bepalen."""
    naam = 'KlSignalisatieReferentiepuntType'
    label = 'Signalisatie referentiepunt type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSignalisatieReferentiepuntType'
    definition = 'Een keuzelijst om het referentiepunt type te bepalen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSignalisatieReferentiepuntType'
    options = {
        'hectometerpalen-in-kunststof': KeuzelijstWaarde(invulwaarde='hectometerpalen-in-kunststof',
                                                         label='hectometerpalen in kunststof',
                                                         definitie='Een kleine paal in kunststof die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpalen-in-kunststof'),
        'hectometerpunt-aan-ronde-steun': KeuzelijstWaarde(invulwaarde='hectometerpunt-aan-ronde-steun',
                                                           label='hectometerpunt aan ronde steun',
                                                           definitie='Een hectometerbord bevestigd aan een ronde steun die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-aan-ronde-steun'),
        'hectometerpunt-op-horizontale-wand': KeuzelijstWaarde(invulwaarde='hectometerpunt-op-horizontale-wand',
                                                               label='hectometerpunt op horizontale wand',
                                                               definitie='Een hectometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke 100 meter langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/hectometerpunt-op-horizontale-wand'),
        'kilometerpalen-in-kunststof': KeuzelijstWaarde(invulwaarde='kilometerpalen-in-kunststof',
                                                        label='kilometerpalen in kunststof',
                                                        definitie='Een kleine paal in kunststof die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpalen-in-kunststof'),
        'kilometerpunt-aan-ronde-steun': KeuzelijstWaarde(invulwaarde='kilometerpunt-aan-ronde-steun',
                                                          label='kilometerpunt aan ronde steun',
                                                          definitie='Een kilometerbord bevestigd aan een ronde steun die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-aan-ronde-steun'),
        'kilometerpunt-op-horizontale-wand': KeuzelijstWaarde(invulwaarde='kilometerpunt-op-horizontale-wand',
                                                              label='kilometerpunt op horizontale wand',
                                                              definitie='Een kilometerbord bevestigd tegen een horizontale wand (zoals bv een New Jersey) die op elke kilometer langs wegen staat en waarop de afstand tot een bepaald startpunt is aangegeven.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSignalisatieReferentiepuntType/kilometerpunt-op-horizontale-wand')
    }

