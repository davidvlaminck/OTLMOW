# coding=utf-8
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
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/andere'),
        'baert': KeuzelijstWaarde(invulwaarde='baert',
                                  label='baert',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/baert'),
        'industrielle-Borraine': KeuzelijstWaarde(invulwaarde='industrielle-Borraine',
                                                  label='industrielle Borraine',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/industrielle-Borraine'),
        'metalogalva': KeuzelijstWaarde(invulwaarde='metalogalva',
                                        label='metalogalva',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/metalogalva'),
        'petitJean': KeuzelijstWaarde(invulwaarde='petitJean',
                                      label='petitJean',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/petitJean'),
        'safetyProducts': KeuzelijstWaarde(invulwaarde='safetyProducts',
                                           label='safetyProducts',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/safetyProducts'),
        'valmont': KeuzelijstWaarde(invulwaarde='valmont',
                                    label='valmont',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/valmont')
    }

