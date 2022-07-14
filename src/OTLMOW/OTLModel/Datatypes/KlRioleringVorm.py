# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringVorm(KeuzelijstField):
    """Vormen van de riolering."""
    naam = 'KlRioleringVorm'
    label = 'Riolering vorm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringVorm'
    definition = 'Vormen van de riolering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringVorm'
    options = {
        'achthoekig': KeuzelijstWaarde(invulwaarde='achthoekig',
                                       label='achthoekig',
                                       status='ingebruik',
                                       definitie='Achthoekig',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/achthoekig'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   definitie='Andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/andere'),
        'cirkelvormig': KeuzelijstWaarde(invulwaarde='cirkelvormig',
                                         label='cirkelvormig',
                                         status='ingebruik',
                                         definitie='Cirkelvormig',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/cirkelvormig'),
        'cunette': KeuzelijstWaarde(invulwaarde='cunette',
                                    label='cunette',
                                    status='ingebruik',
                                    definitie='Cunette',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/cunette'),
        'driehoekig': KeuzelijstWaarde(invulwaarde='driehoekig',
                                       label='driehoekig',
                                       status='ingebruik',
                                       definitie='Driehoekig',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/driehoekig'),
        'eivormig': KeuzelijstWaarde(invulwaarde='eivormig',
                                     label='eivormig',
                                     status='ingebruik',
                                     definitie='Eivormig',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/eivormig'),
        'gewelf': KeuzelijstWaarde(invulwaarde='gewelf',
                                   label='gewelf',
                                   status='ingebruik',
                                   definitie='Gewelf',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/gewelf'),
        'ovaal': KeuzelijstWaarde(invulwaarde='ovaal',
                                  label='ovaal',
                                  status='ingebruik',
                                  definitie='Ovaal',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/ovaal'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='ingebruik',
                                        definitie='Rechthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/rechthoekig'),
        'u-vorm': KeuzelijstWaarde(invulwaarde='u-vorm',
                                   label='u-vorm',
                                   status='ingebruik',
                                   definitie='U-vorm',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/u-vorm'),
        'vierkant': KeuzelijstWaarde(invulwaarde='vierkant',
                                     label='vierkant',
                                     status='ingebruik',
                                     definitie='Vierkant',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/vierkant'),
        'zeshoekig': KeuzelijstWaarde(invulwaarde='zeshoekig',
                                      label='zeshoekig',
                                      status='ingebruik',
                                      definitie='Zeshoekig',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringVorm/zeshoekig')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

