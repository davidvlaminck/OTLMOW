# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordPKModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordPKModelnaam'
    label = 'Dyn bord PK modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordPKModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van dynamische Pijl-Kruis borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordPKModelnaam'
    options = {
        'PK-08J03': KeuzelijstWaarde(invulwaarde='PK-08J03',
                                     label='PK-08J03',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-08J03'),
        'PK-LHT': KeuzelijstWaarde(invulwaarde='PK-LHT',
                                   label='PK-LHT',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-LHT'),
        'PK-Tidal': KeuzelijstWaarde(invulwaarde='PK-Tidal',
                                     label='PK-Tidal',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordPKModelnaam/PK-Tidal')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordPKModelnaam.get_dummy_data()

