# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOMerk(KeuzelijstField):
    """Het merk van de calamiteitendoorsteek."""
    naam = 'KlCADOMerk'
    label = 'Calamiteitendoorsteek merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOMerk'
    definition = 'Het merk van de calamiteitendoorsteek.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOMerk'
    options = {
    }

