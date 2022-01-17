# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-aanzuigunit'),
        'dwarsventilatie-inblaasunit': KeuzelijstWaarde(invulwaarde='dwarsventilatie-inblaasunit',
                                                        label='dwarsventilatie inblaasunit',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-inblaasunit'),
        'langsventilator': KeuzelijstWaarde(invulwaarde='langsventilator',
                                            label='langsventilator',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/langsventilator')
    }

