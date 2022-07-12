# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetonmilieuklasse(KeuzelijstField):
    """Milieuklasse (X-klasse) waaraan het beton wordt blootgesteld."""
    naam = 'KlBetonmilieuklasse'
    label = 'Betonmilieuklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlBetonmilieuklasse'
    definition = 'Milieuklasse (X-klasse) waaraan het beton wordt blootgesteld.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetonmilieuklasse'
    options = {
        'x-0': KeuzelijstWaarde(invulwaarde='x-0',
                                label='X0',
                                status='ingebruik',
                                definitie='Geen risico op corrosie of aantasting, voor beton zonder wapening of ingesloten metalen, behalve bij vorst, dooi of chemische aantasting.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-0'),
        'x-a-1': KeuzelijstWaarde(invulwaarde='x-a-1',
                                  label='XA1',
                                  status='ingebruik',
                                  definitie='Chemische aantasting (Aggressive) : zwak agressieve omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-1'),
        'x-a-2': KeuzelijstWaarde(invulwaarde='x-a-2',
                                  label='XA2',
                                  status='ingebruik',
                                  definitie='Chemische aantasting (Aggressive) : matig agressieve omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-2'),
        'x-a-3': KeuzelijstWaarde(invulwaarde='x-a-3',
                                  label='XA3',
                                  status='ingebruik',
                                  definitie='Chemische aantasting (Aggressive) : sterk agressieve omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-a-3'),
        'x-c-1': KeuzelijstWaarde(invulwaarde='x-c-1',
                                  label='XC1',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door carbonatatie (Carbonatation) : droge of blijvend natte omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-1'),
        'x-c-2': KeuzelijstWaarde(invulwaarde='x-c-2',
                                  label='XC2',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door carbonatatie (Carbonatation) : natte omgeving die zelden droog is.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-2'),
        'x-c-3': KeuzelijstWaarde(invulwaarde='x-c-3',
                                  label='XC3',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door carbonatatie (Carbonatation) : omgeving met matige vochtigheid.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-3'),
        'x-c-4': KeuzelijstWaarde(invulwaarde='x-c-4',
                                  label='XC4',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door carbonatatie (Carbonatation) : wisselend natte en droge omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-c-4'),
        'x-d-1': KeuzelijstWaarde(invulwaarde='x-d-1',
                                  label='XD1',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : omgeving met matige vochtigheid.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-1'),
        'x-d-2': KeuzelijstWaarde(invulwaarde='x-d-2',
                                  label='XD2',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : natte omgeving die zelden droog is.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-2'),
        'x-d-3': KeuzelijstWaarde(invulwaarde='x-d-3',
                                  label='XD3',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden anders dan afkomstig uit zeewater (dooizouten, De-icing salts) : wisselend natte en droge omgeving.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-d-3'),
        'x-f-1': KeuzelijstWaarde(invulwaarde='x-f-1',
                                  label='XF1',
                                  status='ingebruik',
                                  definitie='Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving niet-volledig verzadigd met water, zonder dooizouten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-1'),
        'x-f-2': KeuzelijstWaarde(invulwaarde='x-f-2',
                                  label='XF2',
                                  status='ingebruik',
                                  definitie='Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving niet-volledig verzadigd met water, met dooizouten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-2'),
        'x-f-3': KeuzelijstWaarde(invulwaarde='x-f-3',
                                  label='XF3',
                                  status='ingebruik',
                                  definitie='Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving verzadigd met water, zonder dooizouten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-3'),
        'x-f-4': KeuzelijstWaarde(invulwaarde='x-f-4',
                                  label='XF4',
                                  status='ingebruik',
                                  definitie='Aantasting door vorst-/dooi-wisseling met of zonder dooizouten (Frost) : omgeving verzadigd met water, met dooizouten.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-f-4'),
        'x-s-1': KeuzelijstWaarde(invulwaarde='x-s-1',
                                  label='XS1',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden (zeewater, Seawater) : omgeving met zouthoudende lucht.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-1'),
        'x-s-2': KeuzelijstWaarde(invulwaarde='x-s-2',
                                  label='XS2',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden (zeewater, Seawater) : blijvend onder zeewater.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-2'),
        'x-s-3': KeuzelijstWaarde(invulwaarde='x-s-3',
                                  label='XS3',
                                  status='ingebruik',
                                  definitie='Corrosie ingeleid door chloriden (zeewater, Seawater) : getijde-, spat- en stuifzone.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetonmilieuklasse/x-s-3')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBetonmilieuklasse.get_dummy_data()

