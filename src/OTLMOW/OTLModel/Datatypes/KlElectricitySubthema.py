# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlElectricitySubthema(KeuzelijstField):
    """Lijst voor classificatie van elektrische kabels en appurtenances."""
    naam = 'KlElectricitySubthema'
    label = 'Electricity subthema'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlElectricitySubthema'
    definition = 'Lijst voor classificatie van elektrische kabels en appurtenances.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElectricitySubthema'
    options = {
        'elektriciteitdistributiehoogspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributiehoogspanning',
                                                                 label='elektriciteitDistributieHoogspanning',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributiehoogspanning'),
        'elektriciteitdistributielaagspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributielaagspanning',
                                                                 label='elektriciteitDistributieLaagspanning',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributielaagspanning'),
        'elektriciteitopenbareverlichting': KeuzelijstWaarde(invulwaarde='elektriciteitopenbareverlichting',
                                                             label='elektriciteitOpenbareVerlichting',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitopenbareverlichting'),
        'elektriciteittransport': KeuzelijstWaarde(invulwaarde='elektriciteittransport',
                                                   label='elektriciteitTransport',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransport'),
        'elektriciteittransportplaatselijk': KeuzelijstWaarde(invulwaarde='elektriciteittransportplaatselijk',
                                                              label='elektriciteitTransportPlaatselijk',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransportplaatselijk'),
        'elektriciteitverkeershandhavingssystemen': KeuzelijstWaarde(invulwaarde='elektriciteitverkeershandhavingssystemen',
                                                                     label='elektriciteitVerkeershandhavingssystemen',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeershandhavingssystemen'),
        'elektriciteitverkeerslichten': KeuzelijstWaarde(invulwaarde='elektriciteitverkeerslichten',
                                                         label='elektriciteitVerkeerslichten',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeerslichten')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlElectricitySubthema.get_dummy_data()

