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
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerExoten'
    options = {
        'afbakenen': KeuzelijstWaarde(invulwaarde='afbakenen',
                                      label='afbakenen',
                                      status='ingebruik',
                                      definitie='Afbakenen van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afbakenen'),
        'afdekken-EPDM-folie': KeuzelijstWaarde(invulwaarde='afdekken-EPDM-folie',
                                                label='afdekken EPDM folie',
                                                status='ingebruik',
                                                definitie='Afdekken met EPDM folie van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afdekken-EPDM-folie'),
        'chemisch-behandelen': KeuzelijstWaarde(invulwaarde='chemisch-behandelen',
                                                label='chemisch behandelen',
                                                status='ingebruik',
                                                definitie='Chemisch behandelen van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/chemisch-behandelen'),
        'machinaal-maaien': KeuzelijstWaarde(invulwaarde='machinaal-maaien',
                                             label='machinaal maaien',
                                             status='ingebruik',
                                             definitie='Machinaal maaien van exoten.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/machinaal-maaien'),
        'manueel-maaien': KeuzelijstWaarde(invulwaarde='manueel-maaien',
                                           label='manueel maaien',
                                           status='ingebruik',
                                           definitie='Manueel maaien van exoten.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/manueel-maaien'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='ingebruik',
                                       definitie='Niets doen met betrekken tot het beheer van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/niets-doen'),
        'uitgraven': KeuzelijstWaarde(invulwaarde='uitgraven',
                                      label='uitgraven',
                                      status='ingebruik',
                                      definitie='Uitgraven van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitgraven'),
        'uitspitten': KeuzelijstWaarde(invulwaarde='uitspitten',
                                       label='uitspitten',
                                       status='ingebruik',
                                       definitie='Uitspitten van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitspitten')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

