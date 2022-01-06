# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCADOMerk(Keuzelijst):
    """Het merk van de calamiteitendoorsteek."""

    def __init__(self):
        super().__init__(naam="KlCADOMerk",
                         label="Calamiteitendoorsteek merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCADOMerk",
                         definition="Het merk van de calamiteitendoorsteek.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCADOMerk")

