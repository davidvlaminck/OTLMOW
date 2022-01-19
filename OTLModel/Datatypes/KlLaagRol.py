# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLaagRol(KeuzelijstField):
    """De mogelijke rollen van de laag."""
    naam = 'KlLaagRol'
    label = 'Laag rol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLaagRol'
    definition = 'De mogelijke rollen van de laag.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLaagRol'
    options = {
        'aanvulling': KeuzelijstWaarde(invulwaarde='aanvulling',
                                       label='aanvulling',
                                       definitie='De laag als aanvulling.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/aanvulling'),
        'bed-van-bestrating': KeuzelijstWaarde(invulwaarde='bed-van-bestrating',
                                               label='bed van bestrating',
                                               definitie="Dit betekent hetzelfde als 'straatlaag'. Gelieve voor deze optie 'straatlaag' aan te duiden als keuzemogelijkheid!",
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/bed-van-bestrating'),
        'fundering': KeuzelijstWaarde(invulwaarde='fundering',
                                      label='fundering',
                                      definitie='De laag als fundering.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/fundering'),
        'fundering-voor-lijnvormige-elementen': KeuzelijstWaarde(invulwaarde='fundering-voor-lijnvormige-elementen',
                                                                 label='fundering voor lijnvormige elementen',
                                                                 definitie='De laag als fundering voor lijnvormige elementen.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/fundering-voor-lijnvormige-elementen'),
        'omhulling': KeuzelijstWaarde(invulwaarde='omhulling',
                                      label='omhulling',
                                      definitie='De laag als omhulling.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/omhulling'),
        'onderfundering': KeuzelijstWaarde(invulwaarde='onderfundering',
                                           label='onderfundering',
                                           definitie='De laag als onderfundering.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/onderfundering'),
        'straatlaag': KeuzelijstWaarde(invulwaarde='straatlaag',
                                       label='straatlaag',
                                       definitie='De laag als straatlaag',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/straatlaag'),
        'verharding': KeuzelijstWaarde(invulwaarde='verharding',
                                       label='verharding',
                                       definitie='De laag als verharding.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/verharding'),
        'wapening': KeuzelijstWaarde(invulwaarde='wapening',
                                     label='wapening',
                                     definitie='De laag als wapening en/of bescherming.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLaagRol/wapening')
    }

