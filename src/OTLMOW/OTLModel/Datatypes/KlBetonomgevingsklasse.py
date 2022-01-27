# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetonomgevingsklasse(KeuzelijstField):
    """Omgevingsklasse waaraan het beton wordt blootgesteld."""
    naam = 'KlBetonomgevingsklasse'
    label = 'Betonomgevingsklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBetonomgevingsklasse'
    definition = 'Omgevingsklasse waaraan het beton wordt blootgesteld.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonomgevingsklasse'
    options = {
        'e-0': KeuzelijstWaarde(invulwaarde='e-0',
                                label='E0',
                                definitie='Niet schadelijk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-0'),
        'e-a-1': KeuzelijstWaarde(invulwaarde='e-a-1',
                                  label='EA1',
                                  definitie='Zwak agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-1'),
        'e-a-2': KeuzelijstWaarde(invulwaarde='e-a-2',
                                  label='EA2',
                                  definitie='Middelmatig agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-2'),
        'e-a-3': KeuzelijstWaarde(invulwaarde='e-a-3',
                                  label='EA3',
                                  definitie='Sterk agressieve chemische omgeving volgens tabel 2 van NBN EN 206-1:2001.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-a-3'),
        'e-e-1': KeuzelijstWaarde(invulwaarde='e-e-1',
                                  label='EE1',
                                  definitie='Buitenomgeving : geen vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-1'),
        'e-e-2': KeuzelijstWaarde(invulwaarde='e-e-2',
                                  label='EE2',
                                  definitie='Buitenomgeving : vorst, geen contact met regen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-2'),
        'e-e-3': KeuzelijstWaarde(invulwaarde='e-e-3',
                                  label='EE3',
                                  definitie='Buitenomgeving : vorst, contact met regen.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-3'),
        'e-e-4': KeuzelijstWaarde(invulwaarde='e-e-4',
                                  label='EE4',
                                  definitie='Buitenomgeving : vorst en dooizouten (aanwezigheid van ter plaatse ontdooid of opspattend of aflopend dooizouthoudend water).',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-e-4'),
        'e-s-1': KeuzelijstWaarde(invulwaarde='e-s-1',
                                  label='ES1',
                                  definitie='Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en geen contact met vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-1'),
        'e-s-2': KeuzelijstWaarde(invulwaarde='e-s-2',
                                  label='ES2',
                                  definitie='Zeeomgeving : geen contact met zeewater, wel contact met zeelucht (tot 3 km van de kust) en/of brak water, en wel contact met vorst.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-2'),
        'e-s-3': KeuzelijstWaarde(invulwaarde='e-s-3',
                                  label='ES3',
                                  definitie='Zeeomgeving : contact met zeewater en ondergedompeld.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-3'),
        'e-s-4': KeuzelijstWaarde(invulwaarde='e-s-4',
                                  label='ES4',
                                  definitie='Zeeomgeving : contact met zeewater en getijden- en spatzone.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/e-s-4'),
        'ei': KeuzelijstWaarde(invulwaarde='ei',
                               label='EI',
                               definitie='Binnenomgeving.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonomgevingsklasse/ei')
    }

