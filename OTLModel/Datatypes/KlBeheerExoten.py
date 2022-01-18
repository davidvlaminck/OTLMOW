# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                      definitie='Afbakenen van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afbakenen'),
        'afdekken-EPDM-folie': KeuzelijstWaarde(invulwaarde='afdekken-EPDM-folie',
                                                label='afdekken EPDM folie',
                                                definitie='Afdekken met EPDM folie van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afdekken-EPDM-folie'),
        'chemisch-behandelen': KeuzelijstWaarde(invulwaarde='chemisch-behandelen',
                                                label='chemisch behandelen',
                                                definitie='Chemisch behandelen van exoten.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/chemisch-behandelen'),
        'machinaal-maaien': KeuzelijstWaarde(invulwaarde='machinaal-maaien',
                                             label='machinaal maaien',
                                             definitie='Machinaal maaien van exoten.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/machinaal-maaien'),
        'manueel-maaien': KeuzelijstWaarde(invulwaarde='manueel-maaien',
                                           label='manueel maaien',
                                           definitie='Manueel maaien van exoten.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/manueel-maaien'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       definitie='Niets doen met betrekken tot het beheer van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/niets-doen'),
        'uitgraven': KeuzelijstWaarde(invulwaarde='uitgraven',
                                      label='uitgraven',
                                      definitie='Uitgraven van exoten.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitgraven'),
        'uitspitten': KeuzelijstWaarde(invulwaarde='uitspitten',
                                       label='uitspitten',
                                       definitie='Uitspitten van exoten.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitspitten')
    }

