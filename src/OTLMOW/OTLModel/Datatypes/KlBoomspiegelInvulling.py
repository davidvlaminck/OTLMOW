# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomspiegelInvulling(KeuzelijstField):
    """Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst."""
    naam = 'KlBoomspiegelInvulling'
    label = 'Boomspiegel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomspiegelInvulling'
    definition = 'Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomspiegelInvulling'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   definitie='De boomspiegel bestaat uit ander materiaal dan opgelijst',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/andere'),
        'beplanting': KeuzelijstWaarde(invulwaarde='beplanting',
                                       label='beplanting',
                                       definitie='De boomspiegel bestaat voornamelijk uit sierbeplanting of houtige vegetatie',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/beplanting'),
        'biologisch-afbreekbaar-doek-PLA': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbaar-doek-PLA',
                                                            label='biologisch afbreekbaar doek PLA',
                                                            definitie='Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in PLA.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-PLA'),
        'biologisch-afbreekbaar-doek-jute': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbaar-doek-jute',
                                                             label='biologisch afbreekbaar doek jute',
                                                             definitie='Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in jute.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-jute'),
        'boomschors': KeuzelijstWaarde(invulwaarde='boomschors',
                                       label='boomschors',
                                       definitie='Afdekking van de bodem rond de boom met boomschors.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/boomschors'),
        'gras': KeuzelijstWaarde(invulwaarde='gras',
                                 label='gras',
                                 definitie='De boomspiegel bestaat voornamelijk uit grazige vegetatie die gemaaid kan worden',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/gras'),
        'groencompost': KeuzelijstWaarde(invulwaarde='groencompost',
                                         label='groencompost',
                                         definitie='Afdekking van de bodem rond de boom met groencompost.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/groencompost'),
        'houtsnippers': KeuzelijstWaarde(invulwaarde='houtsnippers',
                                         label='houtsnippers',
                                         definitie='Afdekking van de bodem rond de boom met houtsnippers.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/houtsnippers'),
        'kaal': KeuzelijstWaarde(invulwaarde='kaal',
                                 label='kaal',
                                 definitie='De boomspiegel is kaal of licht begroeid met onkruid (<25%) en word niet gemaaid',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/kaal'),
        'minerale-mulch': KeuzelijstWaarde(invulwaarde='minerale-mulch',
                                           label='minerale mulch',
                                           definitie='De boomspiegel bestaat uit een bodembedekking van minerale oorsprong (vb. grind, dolomiet)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/minerale-mulch'),
        'rooster': KeuzelijstWaarde(invulwaarde='rooster',
                                    label='rooster',
                                    definitie='De boomspiegel is een rooster',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/rooster'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       definitie='In de boomspiegel is verharding aanwezig tot op minder dan 30cm van de stamvoet',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/verharding')
    }

