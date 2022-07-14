# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCabineStandaardtype(KeuzelijstField):
    """Veel voorkomende types van cabines."""
    naam = 'KlCabineStandaardtype'
    label = 'Cabine standaardtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineStandaardtype'
    definition = 'Veel voorkomende types van cabines.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineStandaardtype'
    options = {
        'aluminium-betreedbaar': KeuzelijstWaarde(invulwaarde='aluminium-betreedbaar',
                                                  label='aluminium betreedbaar',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-betreedbaar'),
        'aluminium-niet-betreedbaar': KeuzelijstWaarde(invulwaarde='aluminium-niet-betreedbaar',
                                                       label='aluminium niet betreedbaar',
                                                       status='ingebruik',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-niet-betreedbaar'),
        'beton-betreedbaar': KeuzelijstWaarde(invulwaarde='beton-betreedbaar',
                                              label='beton betreedbaar',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-betreedbaar'),
        'beton-niet-betreedbaar-(compactstation)': KeuzelijstWaarde(invulwaarde='beton-niet-betreedbaar-(compactstation)',
                                                                    label='beton niet betreedbaar (compactstation)',
                                                                    status='ingebruik',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-niet-betreedbaar-(compactstation)'),
        'gemetst-betreedbaar': KeuzelijstWaarde(invulwaarde='gemetst-betreedbaar',
                                                label='gemetst betreedbaar',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/gemetst-betreedbaar'),
        'lokaal-in-een-gebouw': KeuzelijstWaarde(invulwaarde='lokaal-in-een-gebouw',
                                                 label='lokaal in een gebouw',
                                                 status='ingebruik',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/lokaal-in-een-gebouw')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

