# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieCode(KeuzelijstField):
    """Codes voor de figuratie markering."""
    naam = 'KlFiguratieCode'
    label = 'Figuratie code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCode'
    definition = 'Codes voor de figuratie markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieCode'
    options = {
        'BBK-50': KeuzelijstWaarde(invulwaarde='BBK-50',
                                   label='BBK-50',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Aanduiding bebouwde kom met blokken met snelheidsbeperking van 50',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BBK-50'),
        'BBK-BLOK': KeuzelijstWaarde(invulwaarde='BBK-BLOK',
                                     label='BBK BLOK',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Aanduiding bebouwde kom met blokken.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BBK-BLOK'),
        'BHALTE-GR': KeuzelijstWaarde(invulwaarde='BHALTE-GR',
                                      label='BHALTE-GR',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een lettermarkering BUS met arcering > 22.75 m².',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BHALTE-GR'),
        'BHALTE-KL': KeuzelijstWaarde(invulwaarde='BHALTE-KL',
                                      label='BHALTE-KL',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een lettermarkering BUS met arcering < 22.75 m².',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BHALTE-KL'),
        'BHALTE-WEG': KeuzelijstWaarde(invulwaarde='BHALTE-WEG',
                                       label='BHALTE-WEG',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een lettermarkering BUS zonder arcering',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BHALTE-WEG'),
        'BUS-BOB-DW': KeuzelijstWaarde(invulwaarde='BUS-BOB-DW',
                                       label='BUS BOB DW',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een dwarse lettermarkering BUS op BOB.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BUS-BOB-DW'),
        'BUS-BOB-LS': KeuzelijstWaarde(invulwaarde='BUS-BOB-LS',
                                       label='BUS BOB LS',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een overlangse lettermarkering BUS op BOB.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BUS-BOB-LS'),
        'BUS-DW': KeuzelijstWaarde(invulwaarde='BUS-DW',
                                   label='BUS DW',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een dwarse lettermarkering BUS op de busstrook.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/BUS-DW'),
        'HM': KeuzelijstWaarde(invulwaarde='HM',
                               label='HM',
                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                               definitie='Referentiepuntmarkering hectometer- en kilometeraanduiding.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/HM'),
        'LG-Autocar': KeuzelijstWaarde(invulwaarde='LG-Autocar',
                                       label='LG-Autocar',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Logo autocar',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Autocar'),
        'LG-Brfiets-GR': KeuzelijstWaarde(invulwaarde='LG-Brfiets-GR',
                                          label='LG-Brfiets-GR',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Logo bromfiets groot.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Brfiets-GR'),
        'LG-Brfiets-KL': KeuzelijstWaarde(invulwaarde='LG-Brfiets-KL',
                                          label='LG-Brfiets-KL',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='Logo bromfiets klein.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Brfiets-KL'),
        'LG-Elek-GR': KeuzelijstWaarde(invulwaarde='LG-Elek-GR',
                                       label='LG-Elek-GR',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Elektrische voertuigen logo vergroot.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Elek-GR'),
        'LG-Elek-KL': KeuzelijstWaarde(invulwaarde='LG-Elek-KL',
                                       label='LG-Elek-KL',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Elektrische voertuigen logo verkleind.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Elek-KL'),
        'LG-Elek-N': KeuzelijstWaarde(invulwaarde='LG-Elek-N',
                                      label='LG-Elek-N',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Elektrische voertuigen logo normaal.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Elek-N'),
        'LG-FIETS-GR': KeuzelijstWaarde(invulwaarde='LG-FIETS-GR',
                                        label='LG-FIETS-GR',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een fietslogomarkering groot.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-FIETS-GR'),
        'LG-FIETS-KL': KeuzelijstWaarde(invulwaarde='LG-FIETS-KL',
                                        label='LG-FIETS-KL',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een fietslogomarkering klein.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-FIETS-KL'),
        'LG-MV-GR': KeuzelijstWaarde(invulwaarde='LG-MV-GR',
                                     label='LG-MV-GR',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een mindervalidenlogo groot.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-MV-GR'),
        'LG-MV-KL': KeuzelijstWaarde(invulwaarde='LG-MV-KL',
                                     label='LG-MV-KL',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een mindervalidenlogo klein.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-MV-KL'),
        'LG-MV-N': KeuzelijstWaarde(invulwaarde='LG-MV-N',
                                    label='LG-MV-N',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een mindervalidenlogo normaal.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-MV-N'),
        'LG-Woonwrk': KeuzelijstWaarde(invulwaarde='LG-Woonwrk',
                                       label='LG-Woonwrk',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Logo woon-werkverkeer.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/LG-Woonwrk'),
        'PL-A': KeuzelijstWaarde(invulwaarde='PL-A',
                                 label='PL-A',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een voorsorteringspijl rechtdoor waar een snelheidsbeperking <= 70 km/h geldt.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-A'),
        'PL-A'': KeuzelijstWaarde(invulwaarde='PL-A'',
                                  label='PL-A'',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl rechtdoor waar een snelheidsbeperking >= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-A''),
        'PL-B1': KeuzelijstWaarde(invulwaarde='PL-B1',
                                  label='PL-B1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl rechtdoor + links waar een snelheidsbeperking >= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-B1'),
        'PL-B1'': KeuzelijstWaarde(invulwaarde='PL-B1'',
                                   label='PL-B1'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl rechtdoor + links waar een snelheidsbeperking <= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-B1''),
        'PL-B2': KeuzelijstWaarde(invulwaarde='PL-B2',
                                  label='PL-B2',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl rechtdoor + rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-B2'),
        'PL-B2'': KeuzelijstWaarde(invulwaarde='PL-B2'',
                                   label='PL-B2'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl rechtdoor + rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-B2''),
        'PL-C1': KeuzelijstWaarde(invulwaarde='PL-C1',
                                  label='PL-C1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl links waar een snelheidsbeperking <= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C1'),
        'PL-C1'': KeuzelijstWaarde(invulwaarde='PL-C1'',
                                   label='PL-C1'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl links waar een snelheidsbeperking >= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C1''),
        'PL-C2': KeuzelijstWaarde(invulwaarde='PL-C2',
                                  label='PL-C2',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C2'),
        'PL-C2'': KeuzelijstWaarde(invulwaarde='PL-C2'',
                                   label='PL-C2'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C2''),
        'PL-C3': KeuzelijstWaarde(invulwaarde='PL-C3',
                                  label='PL-C3',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl 2de links waar een snelheidsbeperking <= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C3'),
        'PL-C3'': KeuzelijstWaarde(invulwaarde='PL-C3'',
                                   label='PL-C3'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl 2de links waar een snelheidsbeperking >= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C3''),
        'PL-C3'-oud': KeuzelijstWaarde(invulwaarde='PL-C3'-oud',
                                       label='PL-C3' oud',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een voorsorteringspijl 2de links waar een snelheidsbeperking >= 70 km/h geldt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C3'-oud'),
        'PL-C3-oud': KeuzelijstWaarde(invulwaarde='PL-C3-oud',
                                      label='PL-C3 oud',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een voorsorteringspijl 2de links waar een snelheidsbeperking <= 70 km/h geldt.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C3-oud'),
        'PL-C4': KeuzelijstWaarde(invulwaarde='PL-C4',
                                  label='PL-C4',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl 2de rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C4'),
        'PL-C4'': KeuzelijstWaarde(invulwaarde='PL-C4'',
                                   label='PL-C4'',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een voorsorteringspijl 2de rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C4''),
        'PL-C4'-oud': KeuzelijstWaarde(invulwaarde='PL-C4'-oud',
                                       label='PL-C4' oud',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een voorsorteringspijl 2de rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C4'-oud'),
        'PL-C4-oud': KeuzelijstWaarde(invulwaarde='PL-C4-oud',
                                      label='PL-C4 oud',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een voorsorteringspijl 2de rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-C4-oud'),
        'PL-D': KeuzelijstWaarde(invulwaarde='PL-D',
                                 label='PL-D',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een voorsorteringspijl links + rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-D'),
        'PL-D'': KeuzelijstWaarde(invulwaarde='PL-D'',
                                  label='PL-D'',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl links + rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-D''),
        'PL-E': KeuzelijstWaarde(invulwaarde='PL-E',
                                 label='PL-E',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een voorsorteringspijl rechtdoor + links + rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-E'),
        'PL-E'': KeuzelijstWaarde(invulwaarde='PL-E'',
                                  label='PL-E'',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl rechtdoor + links + rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-E''),
        'PL-F1': KeuzelijstWaarde(invulwaarde='PL-F1',
                                  label='PL-F1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde links.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F1'),
        'PL-F1'-oud': KeuzelijstWaarde(invulwaarde='PL-F1'-oud',
                                       label='PL-F1'-oud',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een voorsorteringspijl links waar een snelheidsbeperking >= 70 km/h geldt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F1'-oud'),
        'PL-F1-oud': KeuzelijstWaarde(invulwaarde='PL-F1-oud',
                                      label='PL-F1-oud',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een voorsorteringspijl links waar een snelheidsbeperking <= 70 km/h geldt.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F1-oud'),
        'PL-F2': KeuzelijstWaarde(invulwaarde='PL-F2',
                                  label='PL-F2',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde rechtdoor.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F2'),
        'PL-F2'-oud': KeuzelijstWaarde(invulwaarde='PL-F2'-oud',
                                       label='PL-F2'-oud',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Een voorsorteringspijl rechts waar een snelheidsbeperking >= 70 km/h geldt.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F2'-oud'),
        'PL-F2-oud': KeuzelijstWaarde(invulwaarde='PL-F2-oud',
                                      label='PL-F2-oud',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Een voorsorteringspijl rechts waar een snelheidsbeperking <= 70 km/h geldt.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F2-oud'),
        'PL-F3': KeuzelijstWaarde(invulwaarde='PL-F3',
                                  label='PL-F3',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde rechts.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F3'),
        'PL-F4': KeuzelijstWaarde(invulwaarde='PL-F4',
                                  label='PL-F4',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde rechtdoor + links.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F4'),
        'PL-F5': KeuzelijstWaarde(invulwaarde='PL-F5',
                                  label='PL-F5',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde rechtdoor + rechts.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F5'),
        'PL-F6': KeuzelijstWaarde(invulwaarde='PL-F6',
                                  label='PL-F6',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor rotonde rechtdoor + links + rechts.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-F6'),
        'PL-G1': KeuzelijstWaarde(invulwaarde='PL-G1',
                                  label='PL-G1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een rijstrookverminderingspijl links voor autosnelwegen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-G1'),
        'PL-G2': KeuzelijstWaarde(invulwaarde='PL-G2',
                                  label='PL-G2',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een rijstrookverminderingspijl rechts voor autosnelwegen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-G2'),
        'PL-G3': KeuzelijstWaarde(invulwaarde='PL-G3',
                                  label='PL-G3',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een rijstrookverminderingspijl links voor niet-autosnelwegen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-G3'),
        'PL-G4': KeuzelijstWaarde(invulwaarde='PL-G4',
                                  label='PL-G4',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een rijstrookverminderingspijl rechts voor niet-autosnelwegen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-G4'),
        'PL-c1': KeuzelijstWaarde(invulwaarde='PL-c1',
                                  label='PL-c1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een voorsorteringspijl voor fietsers links.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-c1'),
        'PL-h': KeuzelijstWaarde(invulwaarde='PL-h',
                                 label='PL-h',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Een kleine dubbele fietspadpijl.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-h'),
        'PL-oud': KeuzelijstWaarde(invulwaarde='PL-oud',
                                   label='PL-oud',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een fietspadpijl.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/PL-oud'),
        'STOP-DW': KeuzelijstWaarde(invulwaarde='STOP-DW',
                                    label='STOP DW',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een dwarse lettermarkering STOP.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/STOP-DW'),
        'STOP-DW-oud': KeuzelijstWaarde(invulwaarde='STOP-DW-oud',
                                        label='STOP DW-oud',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Een dwarse lettermarkering STOP.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/STOP-DW-oud'),
        'TAXI-DW': KeuzelijstWaarde(invulwaarde='TAXI-DW',
                                    label='TAXI DW',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een dwarse lettermarkering TAXI.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/TAXI-DW'),
        'TAXI-LS': KeuzelijstWaarde(invulwaarde='TAXI-LS',
                                    label='TAXI LS',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een overlangse lettermarkering TAXI.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/TAXI-LS'),
        'TRAM-DW': KeuzelijstWaarde(invulwaarde='TRAM-DW',
                                    label='TRAM DW',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een dwarse lettermarkering TRAM.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/TRAM-DW'),
        'TRAM-LS': KeuzelijstWaarde(invulwaarde='TRAM-LS',
                                    label='TRAM LS',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Een overlangse lettermarkering TRAM.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/TRAM-LS'),
        'VB-A21': KeuzelijstWaarde(invulwaarde='VB-A21',
                                   label='VB-A21',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Oversteekplaats voor voetgangers.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-A21'),
        'VB-A23': KeuzelijstWaarde(invulwaarde='VB-A23',
                                   label='VB-A23',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een verkeersbordmarkering schoolkinderen (OFF)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-A23'),
        'VB-A49': KeuzelijstWaarde(invulwaarde='VB-A49',
                                   label='VB-A49',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Kruising sporen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-A49'),
        'VB-B1-GR': KeuzelijstWaarde(invulwaarde='VB-B1-GR',
                                     label='VB-B1-GR',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een omgekeerde driehoekmarkering groot.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-B1-GR'),
        'VB-B1-KL': KeuzelijstWaarde(invulwaarde='VB-B1-KL',
                                     label='VB-B1-KL',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een omgekeerde driehoekmarkering klein.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-B1-KL'),
        'VB-E1': KeuzelijstWaarde(invulwaarde='VB-E1',
                                  label='VB-E1',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Een verkeersbordmarkering parkeerverbod (OFF)',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-E1'),
        'VB-E9i': KeuzelijstWaarde(invulwaarde='VB-E9i',
                                   label='VB-E9i',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Een verkeersbordmarkering parkeerschijf (OFF)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-E9i'),
        'VB-F111': KeuzelijstWaarde(invulwaarde='VB-F111',
                                    label='VB-F111',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Fietsstraat begin.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-F111'),
        'VB-F113': KeuzelijstWaarde(invulwaarde='VB-F113',
                                    label='VB-F113',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Fietsstraat einde.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/VB-F113'),
        'visgraat': KeuzelijstWaarde(invulwaarde='visgraat',
                                     label='visgraat',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Een visgraatmarkering om de verkeersveiligheid te vergroten en kop-staartbotsingen te vermijden (bij mist).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCode/visgraat')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlFiguratieCode.get_dummy_data()

