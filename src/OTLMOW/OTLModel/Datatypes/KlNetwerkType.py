# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkType(KeuzelijstField):
    """Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL."""
    naam = 'KlNetwerkType'
    label = 'Netwerk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkType'
    definition = 'Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkType'
    options = {
        'elektriciteit': KeuzelijstWaarde(invulwaarde='elektriciteit',
                                          label='elektriciteit',
                                          status='ingebruik',
                                          definitie='De Klasse hoort in het elektriciteitsnet.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/elektriciteit'),
        'gemengd': KeuzelijstWaarde(invulwaarde='gemengd',
                                    label='gemengd',
                                    status='ingebruik',
                                    definitie='De Klasse hoort zowel bij het elektriciteitsnet als bij het telecomnet.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/gemengd'),
        'telecommunicatie': KeuzelijstWaarde(invulwaarde='telecommunicatie',
                                             label='telecommunicatie',
                                             status='ingebruik',
                                             definitie='De Klasse hoort in het telecomnet.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/telecommunicatie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerkType.get_dummy_data()

