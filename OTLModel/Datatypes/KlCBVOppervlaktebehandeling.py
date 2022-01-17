# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCBVOppervlaktebehandeling(KeuzelijstField):
    """Oppervalktebehandelingen van de cement/beton verharding."""
    naam = 'KlCBVOppervlaktebehandeling'
    label = 'CBV oppervlaktebehandeling'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCBVOppervlaktebehandeling'
    definition = 'Oppervalktebehandelingen van de cement/beton verharding.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCBVOppervlaktebehandeling'
    options = {
        'Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-': KeuzelijstWaarde(invulwaarde='Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-',
                                                                                  label='Reinigen met water onder hoge druk (minstens 50 bar) ',
                                                                                  definitie='Reinigen met water onder hoge druk (minstens 50 bar) ',
                                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/Reinigen-met-water-onder-hoge-druk-(minstens-50-bar)-'),
        'bezemen': KeuzelijstWaarde(invulwaarde='bezemen',
                                    label='bezemen',
                                    definitie='Bezemen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/bezemen'),
        'eenvoudig-dwars-bezemen': KeuzelijstWaarde(invulwaarde='eenvoudig-dwars-bezemen',
                                                    label='eenvoudig dwars bezemen',
                                                    definitie='Eenvoudig dwars bezemen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-dwars-bezemen'),
        'eenvoudig-langs-bezemen': KeuzelijstWaarde(invulwaarde='eenvoudig-langs-bezemen',
                                                    label='eenvoudig langs bezemen',
                                                    definitie='Eenvoudig langs bezemen',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/eenvoudig-langs-bezemen'),
        'figureren': KeuzelijstWaarde(invulwaarde='figureren',
                                      label='figureren',
                                      definitie='Figureren',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/figureren'),
        'uitwassen-van-het-steenslagskelet': KeuzelijstWaarde(invulwaarde='uitwassen-van-het-steenslagskelet',
                                                              label='uitwassen van het steenslagskelet',
                                                              definitie='Uitwassen van het steenslagskelet',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCBVOppervlaktebehandeling/uitwassen-van-het-steenslagskelet')
    }

