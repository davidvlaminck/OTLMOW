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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorGebruik'
    options = {
        'dwarsventilatie-aanzuigunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-aanzuigunit',
                                                        label='dwarsventilatie aanzuigunit',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-aanzuigunit'),
        'dwarsventilatie-inblaasunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-inblaasunit',
                                                        label='dwarsventilatie inblaasunit',
                                                        status='ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-inblaasunit'),
        'langsventilator': KeuzelijstWaarde(invulwaarde='langsventilator',
                                            label='langsventilator',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/langsventilator')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

