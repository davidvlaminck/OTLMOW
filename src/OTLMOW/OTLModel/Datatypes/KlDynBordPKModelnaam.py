# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordPKModelnaam'
    label = 'Dyn bord PK modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKModelnaam'
    options = {
        'PK-08J03': KeuzelijstWaarde(invulwaarde='PK-08J03',
                                     label='PK-08J03',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-08J03'),
        'PK-LHT': KeuzelijstWaarde(invulwaarde='PK-LHT',
                                   label='PK-LHT',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-LHT'),
        'PK-Tidal': KeuzelijstWaarde(invulwaarde='PK-Tidal',
                                     label='PK-Tidal',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-Tidal')
    }

