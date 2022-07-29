# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastLeverancier(KeuzelijstField):
    """Lijst van mogelijke leveranciers van lichtmasten."""
    naam = 'KlLichtmastLeverancier'
    label = 'Lichtmast leverancier'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastLeverancier'
    definition = 'Lijst van mogelijke leveranciers van lichtmasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastLeverancier'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/andere'),
        'arel': KeuzelijstWaarde(invulwaarde='arel',
                                 label='AREL',
                                 status='ingebruik',
                                 definitie='AREL',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/arel'),
        'baert': KeuzelijstWaarde(invulwaarde='baert',
                                  label='baert',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/baert'),
        'industrielle-Borraine': KeuzelijstWaarde(invulwaarde='industrielle-Borraine',
                                                  label='industrielle Borraine',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/industrielle-Borraine'),
        'metalogalva': KeuzelijstWaarde(invulwaarde='metalogalva',
                                        label='metalogalva',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/metalogalva'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='ingebruik',
                                        definitie='Leverancier is niet gekend',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/niet-gekend'),
        'petitJean': KeuzelijstWaarde(invulwaarde='petitJean',
                                      label='petitJean',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/petitJean'),
        'safetyProducts': KeuzelijstWaarde(invulwaarde='safetyProducts',
                                           label='safetyProducts',
                                           status='ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/safetyProducts'),
        'valmont': KeuzelijstWaarde(invulwaarde='valmont',
                                    label='valmont',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/valmont')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

