# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEDDriverMerk(KeuzelijstField):
    """Het merk van de LED-driver."""
    naam = 'KlLEDDriverMerk'
    label = 'LED-driver merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEDDriverMerk'
    definition = 'Het merk van de LED-driver.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEDDriverMerk'
    options = {
    }

