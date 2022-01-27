# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordRVMSModelnaam'
    label = 'Dyn bord RVMS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSModelnaam'
    options = {
        'RVMS-06I04': KeuzelijstWaarde(invulwaarde='RVMS-06I04',
                                       label='RVMS-06I04',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-06I04'),
        'RVMS-12F05': KeuzelijstWaarde(invulwaarde='RVMS-12F05',
                                       label='RVMS-12F05',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-12F05')
    }

