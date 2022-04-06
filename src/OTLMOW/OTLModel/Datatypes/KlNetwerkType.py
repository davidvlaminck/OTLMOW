# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkType(KeuzelijstField):
    """Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL."""
    naam = 'KlNetwerkType'
    label = 'Netwerk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkType'
    definition = 'Zie ook http://inspire.ec.europa.eu/codelist/UtilityNetworkTypeExtendedValue. Codelijst van types voor nutsvoorzieningennetwerken volgens IMKL.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkType'
    options = {
        'elektriciteit': KeuzelijstWaarde(invulwaarde='elektriciteit',
                                          label='elektriciteit',
                                          definitie='De Klasse hoort in het elektriciteitsnet.',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/elektriciteit'),
        'gemengd': KeuzelijstWaarde(invulwaarde='gemengd',
                                    label='gemengd',
                                    definitie='De Klasse hoort zowel bij het elektriciteitsnet als bij het telecomnet.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/gemengd'),
        'telecommunicatie': KeuzelijstWaarde(invulwaarde='telecommunicatie',
                                             label='telecommunicatie',
                                             definitie='De Klasse hoort in het telecomnet.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkType/telecommunicatie')
    }

