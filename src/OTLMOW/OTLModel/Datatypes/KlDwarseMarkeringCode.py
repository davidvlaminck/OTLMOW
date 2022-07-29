# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDwarseMarkeringCode(KeuzelijstField):
    """Codes van de dwarse markering."""
    naam = 'KlDwarseMarkeringCode'
    label = 'Dwarse markering code'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDwarseMarkeringCode'
    definition = 'Codes van de dwarse markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDwarseMarkeringCode'
    options = {
        'DAMBRD': KeuzelijstWaarde(invulwaarde='DAMBRD',
                                   label='DAMBRD',
                                   status='ingebruik',
                                   definitie='Dambord',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DAMBRD'),
        'DREMPEL-1.2': KeuzelijstWaarde(invulwaarde='DREMPEL-1.2',
                                        label='DREMPEL 1.2',
                                        status='ingebruik',
                                        definitie='Verkeersdrempel markering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DREMPEL-1.2'),
        'DRH-fiets-(0.3)': KeuzelijstWaarde(invulwaarde='DRH-fiets-(0.3)',
                                            label='DRH fiets (0.3)',
                                            status='ingebruik',
                                            definitie='Driehoek fiets',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-fiets-(0.3)'),
        'DRH-std-(0.7)': KeuzelijstWaarde(invulwaarde='DRH-std-(0.7)',
                                          label='DRH std (0.7)',
                                          status='ingebruik',
                                          definitie='Driehoek standaard',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/DRH-std-(0.7)'),
        'FLV': KeuzelijstWaarde(invulwaarde='FLV',
                                label='FLV',
                                status='ingebruik',
                                definitie='Verbindingsmarkering voor fietsers.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FLV'),
        'FOP': KeuzelijstWaarde(invulwaarde='FOP',
                                label='FOP',
                                status='ingebruik',
                                definitie='Fietsoversteekplaats met blokken',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/FOP'),
        'PARKEER': KeuzelijstWaarde(invulwaarde='PARKEER',
                                    label='PARKEER',
                                    status='ingebruik',
                                    definitie='Parkeerstrook',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/PARKEER'),
        'RIBBELSTROOK---AFREMMINGSSTREPEN': KeuzelijstWaarde(invulwaarde='RIBBELSTROOK---AFREMMINGSSTREPEN',
                                                             label='RIBBELSTROOK - AFREMMINGSSTREPEN',
                                                             status='ingebruik',
                                                             definitie='Afremmingsstreep',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/RIBBELSTROOK---AFREMMINGSSTREPEN'),
        'STOPSTRP': KeuzelijstWaarde(invulwaarde='STOPSTRP',
                                     label='STOPSTRP',
                                     status='ingebruik',
                                     definitie='Code voor de stopstreep',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP'),
        'STOPSTRP-OFOS': KeuzelijstWaarde(invulwaarde='STOPSTRP-OFOS',
                                          label='STOPSTRP-OFOS',
                                          status='ingebruik',
                                          definitie='Code voor de stopstreep OFOS',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/STOPSTRP-OFOS'),
        'VOP-(3)': KeuzelijstWaarde(invulwaarde='VOP-(3)',
                                    label='VOP (3)',
                                    status='ingebruik',
                                    definitie='Voetgangers-oversteekplaats (3 meter)',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(3)'),
        'VOP-(4)': KeuzelijstWaarde(invulwaarde='VOP-(4)',
                                    label='VOP (4)',
                                    status='ingebruik',
                                    definitie='Voetgangers-oversteekplaats (4 meter)',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(4)'),
        'VOP-(var)': KeuzelijstWaarde(invulwaarde='VOP-(var)',
                                      label='VOP (var)',
                                      status='ingebruik',
                                      definitie='Voetgangers-oversteekplaats (te meten)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VOP-(var)'),
        'VVA-0.4-(0.6)': KeuzelijstWaarde(invulwaarde='VVA-0.4-(0.6)',
                                          label='VVA 0.4 (0.6)',
                                          status='ingebruik',
                                          definitie='Verdrijvingsvlak (40 % opp. v.h. vlak)',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-0.4-(0.6)'),
        'VVA-1-(2)': KeuzelijstWaarde(invulwaarde='VVA-1-(2)',
                                      label='VVA 1 (2)',
                                      status='ingebruik',
                                      definitie='Verdrijvingsvlak (33 % opp. v.h. vlak)',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDwarseMarkeringCode/VVA-1-(2)')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

