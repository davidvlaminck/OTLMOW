from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCabineMerk(Keuzelijst):
    """Merknamen voor cabines."""

    def __init__(self):
        super().__init__(naam="KlCabineMerk",
                         label="Cabine merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineMerk",
                         definition="Merknamen voor cabines.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineMerk")

