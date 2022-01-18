# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterMetertype(KeuzelijstField):
    """Type meter (mechanisch, elektronisch)."""
    naam = 'KlEnergiemeterMetertype'
    label = 'Elektrisch metertype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEnergiemeterMetertype'
    definition = 'Type meter (mechanisch, elektronisch).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterMetertype'
    options = {
        'elektronisch': KeuzelijstWaarde(invulwaarde='elektronisch',
                                         label='elektronisch',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/elektronisch'),
        'mechanisch': KeuzelijstWaarde(invulwaarde='mechanisch',
                                       label='mechanisch',
                                       definitie='Nakijken bij EVT',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterMetertype/mechanisch')
    }

