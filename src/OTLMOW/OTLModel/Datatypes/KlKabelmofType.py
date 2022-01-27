# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKabelmofType(KeuzelijstField):
    """Types voor kabel- en leidingmoffen."""
    naam = 'KlKabelmofType'
    label = 'Kabelmof type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKabelmofType'
    definition = 'Types voor kabel- en leidingmoffen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKabelmofType'
    options = {
        'geldoos': KeuzelijstWaarde(invulwaarde='geldoos',
                                    label='geldoos',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/geldoos'),
        'gietmof': KeuzelijstWaarde(invulwaarde='gietmof',
                                    label='gietmof',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKabelmofType/gietmof')
    }

