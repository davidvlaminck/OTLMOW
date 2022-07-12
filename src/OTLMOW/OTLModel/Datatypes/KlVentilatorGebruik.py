# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVentilatorGebruik(KeuzelijstField):
    """Keuzelijst die de types van gebruik voor de ventilator aangeeft."""
    naam = 'KlVentilatorGebruik'
    label = 'Gebruikstypes ventilator'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorGebruik'
    definition = 'Keuzelijst die de types van gebruik voor de ventilator aangeeft.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorGebruik'
    options = {
        'dwarsventilatie-aanzuigunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-aanzuigunit',
                                                        label='dwarsventilatie aanzuigunit',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-aanzuigunit'),
        'dwarsventilatie-inblaasunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-inblaasunit',
                                                        label='dwarsventilatie inblaasunit',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-inblaasunit'),
        'langsventilator': KeuzelijstWaarde(invulwaarde='langsventilator',
                                            label='langsventilator',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/langsventilator')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVentilatorGebruik.get_dummy_data()

