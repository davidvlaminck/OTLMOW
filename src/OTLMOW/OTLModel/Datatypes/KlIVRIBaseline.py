# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIVRIBaseline(KeuzelijstField):
    """De specificatieversie van het protocol van de iVRI component."""
    naam = 'KlIVRIBaseline'
    label = 'iVRIBaseline'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlIVRIBaseline'
    definition = 'De specificatieversie van het protocol van de iVRI component.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIBaseline'
    options = {
        'idd-tlc-fi-version-1-3-1': KeuzelijstWaarde(invulwaarde='idd-tlc-fi-version-1-3-1',
                                                     label='IDD TLC-FI version 1.3.1',
                                                     definitie='IDD TLC-FI version 1.3.1',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-3-1')
    }

