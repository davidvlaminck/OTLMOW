# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAIMToestand(KeuzelijstField):
    """Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen."""
    naam = 'KlAIMToestand'
    label = 'AIM toestand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAIMToestand'
    definition = 'Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAIMToestand'
    options = {
        'geannuleerd': KeuzelijstWaarde(invulwaarde='geannuleerd',
                                        label='geannuleerd',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/geannuleerd'),
        'gepland': KeuzelijstWaarde(invulwaarde='gepland',
                                    label='gepland',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/gepland'),
        'in-gebruik': KeuzelijstWaarde(invulwaarde='in-gebruik',
                                       label='in gebruik',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik'),
        'in-ontwerp': KeuzelijstWaarde(invulwaarde='in-ontwerp',
                                       label='in ontwerp',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp'),
        'in-opbouw': KeuzelijstWaarde(invulwaarde='in-opbouw',
                                      label='in opbouw',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw'),
        'overgedragen': KeuzelijstWaarde(invulwaarde='overgedragen',
                                         label='overgedragen',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen'),
        'uit-gebruik': KeuzelijstWaarde(invulwaarde='uit-gebruik',
                                        label='uit gebruik',
                                        status='ingebruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/uit-gebruik'),
        'verwijderd': KeuzelijstWaarde(invulwaarde='verwijderd',
                                       label='verwijderd',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

