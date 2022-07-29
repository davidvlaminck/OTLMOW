# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelconnectorBesturingsconnector(KeuzelijstField):
    """Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking."""
    naam = 'KlVerlichtingstoestelconnectorBesturingsconnector'
    label = 'WV-besturingsconnector'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelconnectorBesturingsconnector'
    definition = 'Type van connector verwerkt in de behuizing van het verlichtingstoestel voor de aansluiting van de module voor lokale afstandsbediening en -bewaking.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelconnectorBesturingsconnector'
    options = {
        'NEMA': KeuzelijstWaarde(invulwaarde='NEMA',
                                 label='NEMA',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/NEMA'),
        'SR': KeuzelijstWaarde(invulwaarde='SR',
                               label='SR',
                               status='ingebruik',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelconnectorBesturingsconnector/SR')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

