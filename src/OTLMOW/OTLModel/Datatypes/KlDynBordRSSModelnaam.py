# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRSSModelnaam(KeuzelijstField):
    """Keuzelijst met de gangbare modelnamen van RSS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""
    naam = 'KlDynBordRSSModelnaam'
    label = 'Dyn bord RSS modelnaam'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRSSModelnaam'
    definition = 'Keuzelijst met de gangbare modelnamen van RSS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRSSModelnaam'
    options = {
        'RSS-02E01': KeuzelijstWaarde(invulwaarde='RSS-02E01',
                                      label='RSS-02E01',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-02E01'),
        'RSS-07J06-V1': KeuzelijstWaarde(invulwaarde='RSS-07J06-V1',
                                         label='RSS-07J06 V1',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-07J06-V1'),
        'RSS-07J06-V2': KeuzelijstWaarde(invulwaarde='RSS-07J06-V2',
                                         label='RSS-07J06 V2',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-07J06-V2'),
        'RSS-09D04': KeuzelijstWaarde(invulwaarde='RSS-09D04',
                                      label='RSS-09D04',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-09D04'),
        'RSS-10G04': KeuzelijstWaarde(invulwaarde='RSS-10G04',
                                      label='RSS-10G04',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-10G04'),
        'RSS-12G01': KeuzelijstWaarde(invulwaarde='RSS-12G01',
                                      label='RSS-12G01',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS-12G01'),
        'RSS1-08J03': KeuzelijstWaarde(invulwaarde='RSS1-08J03',
                                       label='RSS1-08J03',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS1-08J03'),
        'RSS2-08J03': KeuzelijstWaarde(invulwaarde='RSS2-08J03',
                                       label='RSS2-08J03',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS2-08J03'),
        'RSS3-08J03': KeuzelijstWaarde(invulwaarde='RSS3-08J03',
                                       label='RSS3-08J03',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRSSModelnaam/RSS3-08J03')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

