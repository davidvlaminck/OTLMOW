# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDrukknopSoort(KeuzelijstField):
    """Keuzelijst met verschillende soorten drukknoppen."""
    naam = 'KlDrukknopSoort'
    label = 'Drukknop soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDrukknopSoort'
    definition = 'Keuzelijst met verschillende soorten drukknoppen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDrukknopSoort'
    options = {
        'WV-drukknop': KeuzelijstWaarde(invulwaarde='WV-drukknop',
                                        label='WV drukknop',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/WV-drukknop'),
        'combi-v-f-drukknop': KeuzelijstWaarde(invulwaarde='combi-v-f-drukknop',
                                               label='combi v f drukknop',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/combi-v-f-drukknop'),
        'combi-v-vg-drukknop': KeuzelijstWaarde(invulwaarde='combi-v-vg-drukknop',
                                                label='combi v vg drukknop',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/combi-v-vg-drukknop'),
        'fietser-drukknop': KeuzelijstWaarde(invulwaarde='fietser-drukknop',
                                             label='fietser drukknop',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/fietser-drukknop'),
        'ruiter-drukknop': KeuzelijstWaarde(invulwaarde='ruiter-drukknop',
                                            label='ruiter drukknop',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/ruiter-drukknop'),
        'visueel-gehandicapt-drukknop': KeuzelijstWaarde(invulwaarde='visueel-gehandicapt-drukknop',
                                                         label='visueel gehandicapt drukknop',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/visueel-gehandicapt-drukknop'),
        'voetganger-drukknop': KeuzelijstWaarde(invulwaarde='voetganger-drukknop',
                                                label='voetganger drukknop',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/voetganger-drukknop')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

