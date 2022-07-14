# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRechteSteunType(KeuzelijstField):
    """Keuzelijst die de verschillende types rechte steunen aanduidt."""
    naam = 'KlRechteSteunType'
    label = 'Rechte steun type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRechteSteunType'
    definition = 'Keuzelijst die de verschillende types rechte steunen aanduidt.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRechteSteunType'
    options = {
        'VRI-met-zwanehals': KeuzelijstWaarde(invulwaarde='VRI-met-zwanehals',
                                              label='VRI met zwanehals',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/VRI-met-zwanehals'),
        'a-paal': KeuzelijstWaarde(invulwaarde='a-paal',
                                   label='a-paal',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/a-paal'),
        'bi-flash': KeuzelijstWaarde(invulwaarde='bi-flash',
                                     label='bi-flash',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/bi-flash'),
        'd-paal': KeuzelijstWaarde(invulwaarde='d-paal',
                                   label='d-paal',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/d-paal'),
        'variabele-Z30': KeuzelijstWaarde(invulwaarde='variabele-Z30',
                                          label='variabele Z30',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/variabele-Z30')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

