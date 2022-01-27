# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelconnectorBesturingsconnector(KeuzelijstField):
    """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
    naam = 'KlVerlichtingstoestelconnectorBesturingsconnector'
    label = 'WV-besturingsconnector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelconnectorBesturingsconnector'
    definition = 'Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelconnectorBesturingsconnector'
    options = {
        'NEMA': KeuzelijstWaarde(invulwaarde='NEMA',
                                 label='NEMA',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/NEMA'),
        'SR': KeuzelijstWaarde(invulwaarde='SR',
                               label='SR',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/SR')
    }

