# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieType(KeuzelijstField):
    """Types van figuratiemarkering."""
    naam = 'KlFiguratieType'
    label = 'Figuratie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieType'
    definition = 'Types van figuratiemarkering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieType'
    options = {
        '2e-afslag-links-(5m)': KeuzelijstWaarde(invulwaarde='2e-afslag-links-(5m)',
                                                 label='2e afslag links (5m)',
                                                 definitie='Pijl 2e afslag links (5m).',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-links-(5m)'),
        '2e-afslag-links-(7.5m)': KeuzelijstWaarde(invulwaarde='2e-afslag-links-(7.5m)',
                                                   label='2e afslag links (7.5m)',
                                                   definitie='Pijl 2e afslag links (7,5m)',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-links-(7.5m)'),
        '2e-afslag-rechts-(5m)': KeuzelijstWaarde(invulwaarde='2e-afslag-rechts-(5m)',
                                                  label='2e afslag rechts (5m)',
                                                  definitie='Pijl 2e afslag rechts (5m)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-rechts-(5m)'),
        '2e-afslag-rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='2e-afslag-rechts-(7.5m)',
                                                    label='2e afslag rechts (7.5m)',
                                                    definitie='Pijl 2e afslag rechts (7,5m)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-rechts-(7.5m)'),
        'BUS-(dwars-op-BOB)': KeuzelijstWaarde(invulwaarde='BUS-(dwars-op-BOB)',
                                               label='BUS (dwars op BOB)',
                                               definitie='Lettermarkering van bus (dwars op BOB)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(dwars-op-BOB)'),
        'BUS-(dwars-op-busstrook)': KeuzelijstWaarde(invulwaarde='BUS-(dwars-op-busstrook)',
                                                     label='BUS (dwars op busstrook)',
                                                     definitie='Lettermarkering van bus (dwars op busstrook)',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(dwars-op-busstrook)'),
        'BUS-(langs-op-BOB)': KeuzelijstWaarde(invulwaarde='BUS-(langs-op-BOB)',
                                               label='BUS (langs op BOB)',
                                               definitie='Lettermarkering van bus (langs op BOB)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(langs-op-BOB)'),
        'STOP': KeuzelijstWaarde(invulwaarde='STOP',
                                 label='STOP',
                                 definitie='Lettermarkering STOP',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/STOP'),
        'STOP-(smal)': KeuzelijstWaarde(invulwaarde='STOP-(smal)',
                                        label='STOP (smal)',
                                        definitie='Lettermarkering STOP (smal)',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/STOP-(smal)'),
        'TAXI-(dwars)': KeuzelijstWaarde(invulwaarde='TAXI-(dwars)',
                                         label='TAXI (dwars)',
                                         definitie='Lettermarkering van taxiplaats (dwars)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TAXI-(dwars)'),
        'TAXI-(langs)': KeuzelijstWaarde(invulwaarde='TAXI-(langs)',
                                         label='TAXI (langs)',
                                         definitie='Lettermarkering van taxiplaats (langs)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TAXI-(langs)'),
        'TRAM-(dwars)': KeuzelijstWaarde(invulwaarde='TRAM-(dwars)',
                                         label='TRAM (dwars)',
                                         definitie='Lettermarkering van tramhalte (dwars)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TRAM-(dwars)'),
        'TRAM-(langs)': KeuzelijstWaarde(invulwaarde='TRAM-(langs)',
                                         label='TRAM (langs)',
                                         definitie='Lettermarkering van tramhalte (langs)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TRAM-(langs)'),
        'autocar': KeuzelijstWaarde(invulwaarde='autocar',
                                    label='autocar',
                                    definitie='Symbool autocar.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/autocar'),
        'blauwe-zone-(parkeerschijf)': KeuzelijstWaarde(invulwaarde='blauwe-zone-(parkeerschijf)',
                                                        label='blauwe zone (parkeerschijf)',
                                                        definitie='Verkeersbordmarkering blauwe zone (parkeerschijf).',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/blauwe-zone-(parkeerschijf)'),
        'bromfiets-groot': KeuzelijstWaarde(invulwaarde='bromfiets-groot',
                                            label='bromfiets groot',
                                            definitie='Symbool bromfiets groot.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bromfiets-groot'),
        'bromfiets-klein': KeuzelijstWaarde(invulwaarde='bromfiets-klein',
                                            label='bromfiets klein',
                                            definitie='Symbool bromfiets klein.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bromfiets-klein'),
        'bushalte-op-de-rijweg': KeuzelijstWaarde(invulwaarde='bushalte-op-de-rijweg',
                                                  label='bushalte op de rijweg',
                                                  definitie='Lettermarkering bus zonder arcering.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bushalte-op-de-rijweg'),
        'elektrische-voertuigen-normaal': KeuzelijstWaarde(invulwaarde='elektrische-voertuigen-normaal',
                                                           label='elektrische voertuigen normaal',
                                                           definitie='Symbool elektrische voertuigen normaal.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-normaal'),
        'elektrische-voertuigen-vergroot': KeuzelijstWaarde(invulwaarde='elektrische-voertuigen-vergroot',
                                                            label='elektrische voertuigen vergroot',
                                                            definitie='Symbool elektrische voertuigen vergroot.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-vergroot'),
        'elektrische-voertuigen-verkleind': KeuzelijstWaarde(invulwaarde='elektrische-voertuigen-verkleind',
                                                             label='elektrische voertuigen verkleind',
                                                             definitie='Symbool elektrische voertuigen verkleind.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-verkleind'),
        'fietslogo-Groot': KeuzelijstWaarde(invulwaarde='fietslogo-Groot',
                                            label='fietslogo Groot',
                                            definitie='Logomarkering fiestslogo Groot.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietslogo-Groot'),
        'fietslogo-Klein': KeuzelijstWaarde(invulwaarde='fietslogo-Klein',
                                            label='fietslogo Klein',
                                            definitie='Logomarkering fiestslogo Klein.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietslogo-Klein'),
        'fietspadpijl-(klein---dubbele-fietspadpijl)': KeuzelijstWaarde(invulwaarde='fietspadpijl-(klein---dubbele-fietspadpijl)',
                                                                        label='fietspadpijl (klein - dubbele fietspadpijl)',
                                                                        definitie='Pijl Fietspadpijl (klein - dubbele fietspadpijl)',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietspadpijl-(klein---dubbele-fietspadpijl)'),
        'fietspadpijl-(std)': KeuzelijstWaarde(invulwaarde='fietspadpijl-(std)',
                                               label='fietspadpijl (std)',
                                               definitie='Pijl Fietspadpijl (std)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietspadpijl-(std)'),
        'fietsstraat-begin': KeuzelijstWaarde(invulwaarde='fietsstraat-begin',
                                              label='fietsstraat begin',
                                              definitie='Verkeersbord F111 dat het einde van de fietsstraat aanduidt.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsstraat-begin'),
        'fietsstraat-einde': KeuzelijstWaarde(invulwaarde='fietsstraat-einde',
                                              label='fietsstraat einde',
                                              definitie='Verkeersbord F113 dat het einde van de fietsstraat aanduidt.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsstraat-einde'),
        'fietsvoorsortering-Links': KeuzelijstWaarde(invulwaarde='fietsvoorsortering-Links',
                                                     label='fietsvoorsortering Links',
                                                     definitie='Pijl Fietsvoorsortering Links',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsvoorsortering-Links'),
        'groot': KeuzelijstWaarde(invulwaarde='groot',
                                  label='groot',
                                  definitie='Omgekeerde driehoek markering groot type.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/groot'),
        'groter-dan-22.75-m²': KeuzelijstWaarde(invulwaarde='groter-dan-22.75-m²',
                                                label='groter dan 22.75 m²',
                                                definitie='Lettermarkering bus met arcering.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/groter-dan-22.75-m²'),
        'klein': KeuzelijstWaarde(invulwaarde='klein',
                                  label='klein',
                                  definitie='Omgekeerde driehoek markering klein type.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/klein'),
        'kleiner-dan-22.75-m²': KeuzelijstWaarde(invulwaarde='kleiner-dan-22.75-m²',
                                                 label='kleiner dan 22.75 m²',
                                                 definitie='Lettermarkering bus met arcering.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/kleiner-dan-22.75-m²'),
        'kruising-sporen': KeuzelijstWaarde(invulwaarde='kruising-sporen',
                                            label='kruising sporen',
                                            definitie='Aanduiding A49 kruising van een openbare weg door één of meer in de rijbaan aangelegde sporen.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/kruising-sporen'),
        'links-(5m)': KeuzelijstWaarde(invulwaarde='links-(5m)',
                                       label='links (5m)',
                                       definitie='Pijl Links (5m)',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-(5m)'),
        'links-(7.5m)': KeuzelijstWaarde(invulwaarde='links-(7.5m)',
                                         label='links (7.5m)',
                                         definitie='Pijl Links (7,5m)',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-(7.5m)'),
        'links-+-Rechts-(5m)': KeuzelijstWaarde(invulwaarde='links-+-Rechts-(5m)',
                                                label='links + Rechts (5m)',
                                                definitie='Pijl Links + Rechts (5m)',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-+-Rechts-(5m)'),
        'links-+-Rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='links-+-Rechts-(7.5m)',
                                                  label='links + Rechts (7.5m)',
                                                  definitie='Pijl Links + Rechts (7,5m)',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-+-Rechts-(7.5m)'),
        'mindervaliden-logo-klein': KeuzelijstWaarde(invulwaarde='mindervaliden-logo-klein',
                                                     label='mindervaliden logo klein',
                                                     definitie='Logomarkering Mindervaliden klein.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-klein'),
        'mindervaliden-logo-normaal': KeuzelijstWaarde(invulwaarde='mindervaliden-logo-normaal',
                                                       label='mindervaliden logo normaal',
                                                       definitie='Logomarkering Mindervaliden normaal.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-normaal'),
        'mindervaliden-logo-vergroot': KeuzelijstWaarde(invulwaarde='mindervaliden-logo-vergroot',
                                                        label='mindervaliden logo vergroot',
                                                        definitie='Logomarkering Mindervaliden vergroot.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-vergroot'),
        'null': KeuzelijstWaarde(invulwaarde='null',
                                 label='null',
                                 definitie='Geen aanduiding.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/null'),
        'oversteekplaats-voor-voetgangers': KeuzelijstWaarde(invulwaarde='oversteekplaats-voor-voetgangers',
                                                             label='oversteekplaats voor voetgangers',
                                                             definitie='Aanduiding A21 oversteekplaats voor voetgangers.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/oversteekplaats-voor-voetgangers'),
        'parkeerverbod': KeuzelijstWaarde(invulwaarde='parkeerverbod',
                                          label='parkeerverbod',
                                          definitie='Verkeersbordmarkering parkeerverbod.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/parkeerverbod'),
        'rechtdoor-(5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-(5m)',
                                           label='rechtdoor (5m)',
                                           definitie='Pijl rechtdoor (5m)',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-(5m)'),
        'rechtdoor-+-Links-(5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Links-(5m)',
                                                   label='rechtdoor + Links (5m)',
                                                   definitie='Pijl Rechtdoor + Links (5m)',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-(5m)'),
        'rechtdoor-+-Links-(7.5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Links-(7.5m)',
                                                     label='rechtdoor + Links (7.5m)',
                                                     definitie='Pijl Rechtdoor + Links (7,5m)',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-(7.5m)'),
        'rechtdoor-+-Links-+-Rechts-(5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Links-+-Rechts-(5m)',
                                                            label='rechtdoor + Links + Rechts (5m)',
                                                            definitie='Pijl Rechtdoor + Links + Rechts (5m)',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-+-Rechts-(5m)'),
        'rechtdoor-+-Links-+-Rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Links-+-Rechts-(7.5m)',
                                                              label='rechtdoor + Links + Rechts (7.5m)',
                                                              definitie='Pijl Rechtdoor + Links + Rechts (7,5m)',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-+-Rechts-(7.5m)'),
        'rechtdoor-+-Rechts-(5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Rechts-(5m)',
                                                    label='rechtdoor + Rechts (5m)',
                                                    definitie='Pijl Rechtdoor + Rechts (5m)',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Rechts-(5m)'),
        'rechtdoor-+-Rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='rechtdoor-+-Rechts-(7.5m)',
                                                      label='rechtdoor + Rechts (7.5m)',
                                                      definitie='Pijl Rechtdoor + Rechts (7,5m)',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Rechts-(7.5m)'),
        'rechts-(5m)': KeuzelijstWaarde(invulwaarde='rechts-(5m)',
                                        label='rechts (5m)',
                                        definitie='Pijl Rechts (5m)',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechts-(5m)'),
        'rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='rechts-(7.5m)',
                                          label='rechts (7.5m)',
                                          definitie='Pijl Rechts (7,5m)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechts-(7.5m)'),
        'rijstrook-vermindering-links': KeuzelijstWaarde(invulwaarde='rijstrook-vermindering-links',
                                                         label='rijstrook vermindering links',
                                                         definitie='Pijl Rijstrook vermindering links',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rijstrook-vermindering-links'),
        'rijstrook-vermindering-rechts': KeuzelijstWaarde(invulwaarde='rijstrook-vermindering-rechts',
                                                          label='rijstrook vermindering rechts',
                                                          definitie='Pijl Rijstrook vermindering rechts',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rijstrook-vermindering-rechts'),
        'schoolkinderen': KeuzelijstWaarde(invulwaarde='schoolkinderen',
                                           label='schoolkinderen',
                                           definitie='Verkeersbordmarkering schoolkinderen.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/schoolkinderen'),
        'turborotonde-Links': KeuzelijstWaarde(invulwaarde='turborotonde-Links',
                                               label='turborotonde Links',
                                               definitie='Pijl Turborotonde Links',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Links'),
        'turborotonde-Rechtdoor': KeuzelijstWaarde(invulwaarde='turborotonde-Rechtdoor',
                                                   label='turborotonde Rechtdoor',
                                                   definitie='Pijl Turborotonde Rechtdoor',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor'),
        'turborotonde-Rechtdoor-en-Links': KeuzelijstWaarde(invulwaarde='turborotonde-Rechtdoor-en-Links',
                                                            label='turborotonde Rechtdoor en Links',
                                                            definitie='Pijl Turborotonde Rechtdoor en Links',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor-en-Links'),
        'turborotonde-Rechtdoor-en-Rechts': KeuzelijstWaarde(invulwaarde='turborotonde-Rechtdoor-en-Rechts',
                                                             label='turborotonde Rechtdoor en Rechts',
                                                             definitie='Pijl Turborotonde Rechtdoor en Rechts',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor-en-Rechts'),
        'turborotonde-Rechtdoor.-Links-en-rechts': KeuzelijstWaarde(invulwaarde='turborotonde-Rechtdoor.-Links-en-rechts',
                                                                    label='turborotonde Rechtdoor. Links en rechts',
                                                                    definitie='Pijl Turborotonde Rechtdoor, Links en rechts',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor.-Links-en-rechts'),
        'turborotonde-Rechts': KeuzelijstWaarde(invulwaarde='turborotonde-Rechts',
                                                label='turborotonde Rechts',
                                                definitie='Pijl Turborotonde Rechts',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechts'),
        'voorsortering-Links-(5m)': KeuzelijstWaarde(invulwaarde='voorsortering-Links-(5m)',
                                                     label='voorsortering Links (5m)',
                                                     definitie='Pijl Voorsortering Links (5m)',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Links-(5m)'),
        'voorsortering-Links-(7.5m)': KeuzelijstWaarde(invulwaarde='voorsortering-Links-(7.5m)',
                                                       label='voorsortering Links (7.5m)',
                                                       definitie='Pijl Voorsortering Links (7,5m)',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Links-(7.5m)'),
        'voorsortering-Rechts-(5m)': KeuzelijstWaarde(invulwaarde='voorsortering-Rechts-(5m)',
                                                      label='voorsortering Rechts (5m)',
                                                      definitie='Pijl Voorsortering Rechts (5m)',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Rechts-(5m)'),
        'voorsortering-Rechts-(7.5m)': KeuzelijstWaarde(invulwaarde='voorsortering-Rechts-(7.5m)',
                                                        label='voorsortering Rechts (7.5m)',
                                                        definitie='Aanduiding A49 kruising van een openbare weg door één of meer in de rijbaan aangelegde sporen.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Rechts-(7.5m)'),
        'woon-werkverkeer': KeuzelijstWaarde(invulwaarde='woon-werkverkeer',
                                             label='woon-werkverkeer',
                                             definitie='Symbool woon-werkverkeer.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/woon-werkverkeer')
    }

