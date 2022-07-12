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
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastLeverancier'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/andere'),
        'arel': KeuzelijstWaarde(invulwaarde='arel',
                                 label='AREL',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='AREL',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/arel'),
        'baert': KeuzelijstWaarde(invulwaarde='baert',
                                  label='baert',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/baert'),
        'industrielle-Borraine': KeuzelijstWaarde(invulwaarde='industrielle-Borraine',
                                                  label='industrielle Borraine',
                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/industrielle-Borraine'),
        'metalogalva': KeuzelijstWaarde(invulwaarde='metalogalva',
                                        label='metalogalva',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/metalogalva'),
        'niet-gekend': KeuzelijstWaarde(invulwaarde='niet-gekend',
                                        label='niet gekend',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Leverancier is niet gekend',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/niet-gekend'),
        'petitJean': KeuzelijstWaarde(invulwaarde='petitJean',
                                      label='petitJean',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/petitJean'),
        'safetyProducts': KeuzelijstWaarde(invulwaarde='safetyProducts',
                                           label='safetyProducts',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/safetyProducts'),
        'valmont': KeuzelijstWaarde(invulwaarde='valmont',
                                    label='valmont',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/valmont')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlLichtmastLeverancier.get_dummy_data()

