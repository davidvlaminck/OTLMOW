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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlElectricitySubthema'
    options = {
        'elektriciteitdistributiehoogspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributiehoogspanning',
                                                                 label='elektriciteitDistributieHoogspanning',
                                                                 status='ingebruik',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributiehoogspanning'),
        'elektriciteitdistributielaagspanning': KeuzelijstWaarde(invulwaarde='elektriciteitdistributielaagspanning',
                                                                 label='elektriciteitDistributieLaagspanning',
                                                                 status='ingebruik',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitdistributielaagspanning'),
        'elektriciteitopenbareverlichting': KeuzelijstWaarde(invulwaarde='elektriciteitopenbareverlichting',
                                                             label='elektriciteitOpenbareVerlichting',
                                                             status='ingebruik',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitopenbareverlichting'),
        'elektriciteittransport': KeuzelijstWaarde(invulwaarde='elektriciteittransport',
                                                   label='elektriciteitTransport',
                                                   status='ingebruik',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransport'),
        'elektriciteittransportplaatselijk': KeuzelijstWaarde(invulwaarde='elektriciteittransportplaatselijk',
                                                              label='elektriciteitTransportPlaatselijk',
                                                              status='ingebruik',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteittransportplaatselijk'),
        'elektriciteitverkeershandhavingssystemen': KeuzelijstWaarde(invulwaarde='elektriciteitverkeershandhavingssystemen',
                                                                     label='elektriciteitVerkeershandhavingssystemen',
                                                                     status='ingebruik',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeershandhavingssystemen'),
        'elektriciteitverkeerslichten': KeuzelijstWaarde(invulwaarde='elektriciteitverkeerslichten',
                                                         label='elektriciteitVerkeerslichten',
                                                         status='ingebruik',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlElectricitySubthema/elektriciteitverkeerslichten')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

