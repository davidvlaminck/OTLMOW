from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHardwareMerk(Keuzelijst):
    """Het merk van de hardware."""

    def __init__(self):
        super().__init__(naam="KlHardwareMerk",
                         label="Hardware merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHardwareMerk",
                         definition="Het merk van de hardware.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHardwareMerk")

