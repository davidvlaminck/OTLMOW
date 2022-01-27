# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringSoort(KeuzelijstField):
    """Soorten van dwarse markering."""
    naam = 'KlDwarseMarkeringSoort'
    label = 'Dwarse markering soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringSoort'
    definition = 'Soorten van dwarse markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringSoort'
    options = {
        'afremmingsstreep': KeuzelijstWaarde(invulwaarde='afremmingsstreep',
                                             label='afremmingsstreep',
                                             definitie='Ribbelvlak bestaande uit een aantal permanente dwarse lijnen, ook afremmingsstrepen genoemd',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/afremmingsstreep'),
        'dambord': KeuzelijstWaarde(invulwaarde='dambord',
                                    label='dambord',
                                    definitie='Een dambord bakent de plaats af voorbehouden aan voertuigen van geregelde diensten voor gemeenschappelijk vervoer op een bijzondere overrijdbare bedding of de plaats die eigen beddingen en bijzondere overrijdbare beddingen met elkaar verbinden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/dambord'),
        'driehoek-(Haaientand)': KeuzelijstWaarde(invulwaarde='driehoek-(Haaientand)',
                                                  label='driehoek (Haaientand)',
                                                  definitie='Haaietanden is een markering die de bestuurders aangeeft om voorrang te verlenen aan bestuurders op de kruisende weg.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/driehoek-(Haaientand)'),
        'fietsoversteekplaats-met-blokken-(FOP)': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-blokken-(FOP)',
                                                                   label='fietsoversteekplaats met blokken (FOP)',
                                                                   definitie='Een oversteekplaats voor fietsers gemarkeerd door witte blokken.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/fietsoversteekplaats-met-blokken-(FOP)'),
        'fietsoversteekplaats-met-lijnen-(FOPL)': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-lijnen-(FOPL)',
                                                                   label='fietsoversteekplaats met lijnen (FOPL)',
                                                                   definitie='Een oversteekplaats voor fietsers gemarkeerd door witte evenwijdige lijnen.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/fietsoversteekplaats-met-lijnen-(FOPL)'),
        'onderbroken-verbindingsmarkering': KeuzelijstWaarde(invulwaarde='onderbroken-verbindingsmarkering',
                                                             label='onderbroken verbindingsmarkering',
                                                             definitie='Markering om de geleiding voor de fietsers te verbeteren en het attentieniveau van een afdraaiend voertuig ten opzichte van de fietsers te verhogen.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/onderbroken-verbindingsmarkering'),
        'parkeerstrook': KeuzelijstWaarde(invulwaarde='parkeerstrook',
                                          label='parkeerstrook',
                                          definitie='Een gemarkeerde parkeergelegenheid langs een rijweg.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/parkeerstrook'),
        'stopstreep-(Alg)': KeuzelijstWaarde(invulwaarde='stopstreep-(Alg)',
                                             label='stopstreep (Alg)',
                                             definitie='Een stopstreep is een witte streep die dwars op de rijbaan is aangebracht. Het geeft aan waar de bestuurders moeten stoppen.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/stopstreep-(Alg)'),
        'stopstreep-(OFOS)': KeuzelijstWaarde(invulwaarde='stopstreep-(OFOS)',
                                              label='stopstreep (OFOS)',
                                              definitie='Een stopstreep bij de opgeblazen fietsopstelstrook (OFOS).',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/stopstreep-(OFOS)'),
        'verdrijvingsvlak-(Arcering)': KeuzelijstWaarde(invulwaarde='verdrijvingsvlak-(Arcering)',
                                                        label='verdrijvingsvlak (Arcering)',
                                                        definitie='Keuzelijst voor het bepalen van het type van dwarse markering.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/verdrijvingsvlak-(Arcering)'),
        'verkeersdrempel-markering': KeuzelijstWaarde(invulwaarde='verkeersdrempel-markering',
                                                      label='verkeersdrempel markering',
                                                      definitie='?',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/verkeersdrempel-markering'),
        'voetgangers-oversteekplaats-(VOP)': KeuzelijstWaarde(invulwaarde='voetgangers-oversteekplaats-(VOP)',
                                                              label='voetgangers-oversteekplaats (VOP)',
                                                              definitie='Een locatie op de rijbaan die bestemd is voor voetgangers om over te steken.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringSoort/voetgangers-oversteekplaats-(VOP)')
    }

