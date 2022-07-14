# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieSoort(KeuzelijstField):
    """Soorten van figuratie markering."""
    naam = 'KlFiguratieSoort'
    label = 'Figuratie soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieSoort'
    definition = 'Soorten van figuratie markering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieSoort'
    options = {
        'aanduiding-bebouwde-kom---snelheidsbeperking-(50)': KeuzelijstWaarde(invulwaarde='aanduiding-bebouwde-kom---snelheidsbeperking-(50)',
                                                                              label='aanduiding bebouwde kom - snelheidsbeperking (50)',
                                                                              status='ingebruik',
                                                                              definitie='Aanduiding bebouwde kom met blokken met snelheidsbeperking van 50 (zonder cirkel).',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/aanduiding-bebouwde-kom---snelheidsbeperking-(50)'),
        'aanduiding-bebouwde-kom-met-blokken': KeuzelijstWaarde(invulwaarde='aanduiding-bebouwde-kom-met-blokken',
                                                                label='aanduiding bebouwde kom met blokken',
                                                                status='ingebruik',
                                                                definitie='Aanduiding bebouwde kom met blokken.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/aanduiding-bebouwde-kom-met-blokken'),
        'bushalte-met-arcering': KeuzelijstWaarde(invulwaarde='bushalte-met-arcering',
                                                  label='bushalte met arcering',
                                                  status='ingebruik',
                                                  definitie='Een lettermarkering BUS met arcering.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/bushalte-met-arcering'),
        'bushalte-zonder-arcering': KeuzelijstWaarde(invulwaarde='bushalte-zonder-arcering',
                                                     label='bushalte zonder arcering',
                                                     status='ingebruik',
                                                     definitie='Een lettermarkering BUS zonder arcering.',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/bushalte-zonder-arcering'),
        'hm': KeuzelijstWaarde(invulwaarde='hm',
                               label='hm',
                               status='ingebruik',
                               definitie='Referentiepuntmarkering hectometer- en kilometeraanduiding.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/hm'),
        'letterfiguratiemarkering': KeuzelijstWaarde(invulwaarde='letterfiguratiemarkering',
                                                     label='letterfiguratiemarkering',
                                                     status='ingebruik',
                                                     definitie='Een lettermarking als figuratie zoals BUS, TAXI, TRAM,....',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/letterfiguratiemarkering'),
        'logo': KeuzelijstWaarde(invulwaarde='logo',
                                 label='logo',
                                 status='ingebruik',
                                 definitie='Een markering in de vorm van een logo.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/logo'),
        'omgekeerde-driehoek': KeuzelijstWaarde(invulwaarde='omgekeerde-driehoek',
                                                label='omgekeerde driehoek',
                                                status='ingebruik',
                                                definitie='Een omgekeerde driehoek markering.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/omgekeerde-driehoek'),
        'pijl': KeuzelijstWaarde(invulwaarde='pijl',
                                 label='pijl',
                                 status='ingebruik',
                                 definitie='Een pijlvormige markering.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/pijl'),
        'verkeersbord': KeuzelijstWaarde(invulwaarde='verkeersbord',
                                         label='verkeersbord',
                                         status='ingebruik',
                                         definitie='Een markering in de vorm van een verkeersbord.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/verkeersbord'),
        'visgraatmarkering': KeuzelijstWaarde(invulwaarde='visgraatmarkering',
                                              label='visgraatmarkering',
                                              status='ingebruik',
                                              definitie='Een visgraatmarkering.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/visgraatmarkering')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

