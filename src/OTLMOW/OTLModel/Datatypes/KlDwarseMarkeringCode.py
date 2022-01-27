# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringCode(KeuzelijstField):
    """Codes van de dwarse markering."""
    naam = 'KlDwarseMarkeringCode'
    label = 'Dwarse markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringCode'
    definition = 'Codes van de dwarse markering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringCode'
    options = {
        'DAMBRD': KeuzelijstWaarde(invulwaarde='DAMBRD',
                                   label='DAMBRD',
                                   definitie='Dambord',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DAMBRD'),
        'DREMPEL-1.2': KeuzelijstWaarde(invulwaarde='DREMPEL-1.2',
                                        label='DREMPEL 1.2',
                                        definitie='Verkeersdrempel markering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DREMPEL-1.2'),
        'DRH-fiets-(0.3)': KeuzelijstWaarde(invulwaarde='DRH-fiets-(0.3)',
                                            label='DRH fiets (0.3)',
                                            definitie='Driehoek fiets',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-fiets-(0.3)'),
        'DRH-std-(0.7)': KeuzelijstWaarde(invulwaarde='DRH-std-(0.7)',
                                          label='DRH std (0.7)',
                                          definitie='Driehoek standaard',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-std-(0.7)'),
        'FLV': KeuzelijstWaarde(invulwaarde='FLV',
                                label='FLV',
                                definitie='Verbindingsmarkering voor fietsers.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FLV'),
        'FOP': KeuzelijstWaarde(invulwaarde='FOP',
                                label='FOP',
                                definitie='Fietsoversteekplaats met blokken',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FOP'),
        'PARKEER': KeuzelijstWaarde(invulwaarde='PARKEER',
                                    label='PARKEER',
                                    definitie='Parkeerstrook',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/PARKEER'),
        'RIBBELSTROOK---AFREMMINGSSTREPEN': KeuzelijstWaarde(invulwaarde='RIBBELSTROOK---AFREMMINGSSTREPEN',
                                                             label='RIBBELSTROOK - AFREMMINGSSTREPEN',
                                                             definitie='Afremmingsstreep',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/RIBBELSTROOK---AFREMMINGSSTREPEN'),
        'STOPSTRP': KeuzelijstWaarde(invulwaarde='STOPSTRP',
                                     label='STOPSTRP',
                                     definitie='Code voor de stopstreep',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP'),
        'STOPSTRP-OFOS': KeuzelijstWaarde(invulwaarde='STOPSTRP-OFOS',
                                          label='STOPSTRP-OFOS',
                                          definitie='Code voor de stopstreep OFOS',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP-OFOS'),
        'VOP-(3)': KeuzelijstWaarde(invulwaarde='VOP-(3)',
                                    label='VOP (3)',
                                    definitie='Voetgangers-oversteekplaats (3 meter)',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(3)'),
        'VOP-(4)': KeuzelijstWaarde(invulwaarde='VOP-(4)',
                                    label='VOP (4)',
                                    definitie='Voetgangers-oversteekplaats (4 meter)',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(4)'),
        'VOP-(var)': KeuzelijstWaarde(invulwaarde='VOP-(var)',
                                      label='VOP (var)',
                                      definitie='Voetgangers-oversteekplaats (te meten)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(var)'),
        'VVA-0.4-(0.6)': KeuzelijstWaarde(invulwaarde='VVA-0.4-(0.6)',
                                          label='VVA 0.4 (0.6)',
                                          definitie='Verdrijvingsvlak (40 % opp. v.h. vlak)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-0.4-(0.6)'),
        'VVA-1-(2)': KeuzelijstWaarde(invulwaarde='VVA-1-(2)',
                                      label='VVA 1 (2)',
                                      definitie='Verdrijvingsvlak (33 % opp. v.h. vlak)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-1-(2)')
    }

