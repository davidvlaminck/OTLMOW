# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordZ30Modelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische zone 30 borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordZ30Modelnaam'
    label = 'Z30 modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordZ30Modelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische zone 30 borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordZ30Modelnaam'
    options = {
        'C31-pijl-links': KeuzelijstWaarde(invulwaarde='C31-pijl-links',
                                           label='C31 pijl links',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/C31-pijl-links'),
        'C31-pijl-rechts': KeuzelijstWaarde(invulwaarde='C31-pijl-rechts',
                                            label='C31 pijl rechts',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/C31-pijl-rechts'),
        'C43-50': KeuzelijstWaarde(invulwaarde='C43-50',
                                   label='C43 50',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/C43-50'),
        'C43-50-70': KeuzelijstWaarde(invulwaarde='C43-50-70',
                                      label='C43 50-70',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/C43-50-70'),
        'C43-70': KeuzelijstWaarde(invulwaarde='C43-70',
                                   label='C43 70',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/C43-70'),
        'F4a-30': KeuzelijstWaarde(invulwaarde='F4a-30',
                                   label='F4a 30',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30'),
        'F4a-30-50': KeuzelijstWaarde(invulwaarde='F4a-30-50',
                                      label='F4a 30-50',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-50'),
        'F4a-30-50-70': KeuzelijstWaarde(invulwaarde='F4a-30-50-70',
                                         label='F4a 30-50-70',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-50-70'),
        'F4a-30-50-70-Flash': KeuzelijstWaarde(invulwaarde='F4a-30-50-70-Flash',
                                               label='F4a 30-50-70 Flash',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-50-70-Flash'),
        'F4a-30-50-Flash': KeuzelijstWaarde(invulwaarde='F4a-30-50-Flash',
                                            label='F4a 30-50 Flash',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-50-Flash'),
        'F4a-30-70': KeuzelijstWaarde(invulwaarde='F4a-30-70',
                                      label='F4a 30-70',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-70'),
        'F4a-30-70-Flash': KeuzelijstWaarde(invulwaarde='F4a-30-70-Flash',
                                            label='F4a 30-70 Flash',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4a-30-70-Flash'),
        'F4b-30': KeuzelijstWaarde(invulwaarde='F4b-30',
                                   label='F4b 30',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30'),
        'F4b-30-50': KeuzelijstWaarde(invulwaarde='F4b-30-50',
                                      label='F4b 30-50',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-50'),
        'F4b-30-50-70': KeuzelijstWaarde(invulwaarde='F4b-30-50-70',
                                         label='F4b 30-50-70',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-50-70'),
        'F4b-30-50-70-Flash': KeuzelijstWaarde(invulwaarde='F4b-30-50-70-Flash',
                                               label='F4b 30-50-70 Flash',
                                               status='ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-50-70-Flash'),
        'F4b-30-50-Flash': KeuzelijstWaarde(invulwaarde='F4b-30-50-Flash',
                                            label='F4b 30-50 Flash',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-50-Flash'),
        'F4b-30-70': KeuzelijstWaarde(invulwaarde='F4b-30-70',
                                      label='F4b 30-70',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-70'),
        'F4b-30-70-Flash': KeuzelijstWaarde(invulwaarde='F4b-30-70-Flash',
                                            label='F4b 30-70 Flash',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordZ30Modelnaam/F4b-30-70-Flash')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

