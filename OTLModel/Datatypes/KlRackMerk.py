from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlRackMerk(Keuzelijst):
    """Merken voor racks."""

    def __init__(self):
        super().__init__(naam="KlRackMerk",
                         label="Rack merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRackMerk",
                         definition="Merken voor racks.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRackMerk")

