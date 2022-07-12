# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordVMSModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van VMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordVMSModelnaam'
    label = 'Dyn bord VMS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordVMSModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van VMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordVMSModelnaam'
    options = {
        'VMS-00A09': KeuzelijstWaarde(invulwaarde='VMS-00A09',
                                      label='VMS-00A09',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-00A09'),
        'VMS-07J06': KeuzelijstWaarde(invulwaarde='VMS-07J06',
                                      label='VMS-07J06',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-07J06'),
        'VMS-10G01': KeuzelijstWaarde(invulwaarde='VMS-10G01',
                                      label='VMS-10G01',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-10G01')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDynBordVMSModelnaam.get_dummy_data()

