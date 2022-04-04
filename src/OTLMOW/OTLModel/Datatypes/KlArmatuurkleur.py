# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlArmatuurkleur(KeuzelijstField):
    """De kleur van de zichtbare buitenkant van een verlichtingstoestel."""
    naam = 'KlArmatuurkleur'
    label = 'Armatuurkleur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlArmatuurkleur'
    definition = 'De kleur van de zichtbare buitenkant van een verlichtingstoestel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlArmatuurkleur'
    options = {
        'ral-1023': KeuzelijstWaarde(invulwaarde='ral-1023',
                                     label='RAL 1023',
                                     definitie='Geel - VVOP-mast',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-1023'),
        'ral-2009': KeuzelijstWaarde(invulwaarde='ral-2009',
                                     label='RAL 2009',
                                     definitie='Oranje - kast van trambarelen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-2009'),
        'ral-5017': KeuzelijstWaarde(invulwaarde='ral-5017',
                                     label='RAL 5017',
                                     definitie='Blauw - seinplaat drukknoppen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-5017'),
        'ral-7035': KeuzelijstWaarde(invulwaarde='ral-7035',
                                     label='RAL 7035',
                                     definitie='Grijs - HS-cabines + LS-kasten standaardbestek',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-7035'),
        'ral-7038': KeuzelijstWaarde(invulwaarde='ral-7038',
                                     label='RAL 7038',
                                     definitie='Grijs - masten standaardbestek',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-7038'),
        'ral-7043': KeuzelijstWaarde(invulwaarde='ral-7043',
                                     label='RAL 7043',
                                     definitie='Grijs - masten bijzonder bestek',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-7043'),
        'ral-9003': KeuzelijstWaarde(invulwaarde='ral-9003',
                                     label='RAL 9003',
                                     definitie='Beige - HS-cabines standaardbestek',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-9003'),
        'ral-9005': KeuzelijstWaarde(invulwaarde='ral-9005',
                                     label='RAL 9005',
                                     definitie='Zwart - nummering masten',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-9005'),
        'ral-9007': KeuzelijstWaarde(invulwaarde='ral-9007',
                                     label='RAL 9007',
                                     definitie='Grijs - OV-toestellen',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-9007'),
        'ral-9017': KeuzelijstWaarde(invulwaarde='ral-9017',
                                     label='RAL 9017',
                                     definitie='Zwart - banden VVOP-mast',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlArmatuurkleur/ral-9017')
    }

