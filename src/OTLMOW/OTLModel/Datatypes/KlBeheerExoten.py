# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerExoten(KeuzelijstField):
    """Behandelingswijzen van exoten."""
    naam = 'KlBeheerExoten'
    label = 'Beheer exoten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerExoten'
    definition = 'Behandelingswijzen van exoten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerExoten'
    options = {
        'afbakenen': KeuzelijstWaarde(invulwaarde='afbakenen',
                                      label='afbakenen',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Afbakenen van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afbakenen'),
        'afdekken-EPDM-folie': KeuzelijstWaarde(invulwaarde='afdekken-EPDM-folie',
                                                label='afdekken EPDM folie',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='Afdekken met EPDM folie van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afdekken-EPDM-folie'),
        'chemisch-behandelen': KeuzelijstWaarde(invulwaarde='chemisch-behandelen',
                                                label='chemisch behandelen',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='Chemisch behandelen van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/chemisch-behandelen'),
        'machinaal-maaien': KeuzelijstWaarde(invulwaarde='machinaal-maaien',
                                             label='machinaal maaien',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Machinaal maaien van exoten.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/machinaal-maaien'),
        'manueel-maaien': KeuzelijstWaarde(invulwaarde='manueel-maaien',
                                           label='manueel maaien',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           definitie='Manueel maaien van exoten.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/manueel-maaien'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Niets doen met betrekken tot het beheer van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/niets-doen'),
        'uitgraven': KeuzelijstWaarde(invulwaarde='uitgraven',
                                      label='uitgraven',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Uitgraven van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitgraven'),
        'uitspitten': KeuzelijstWaarde(invulwaarde='uitspitten',
                                       label='uitspitten',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Uitspitten van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitspitten')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBeheerExoten.get_dummy_data()

