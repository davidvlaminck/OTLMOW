from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWeegsensorMerk(Keuzelijst):
    """Het merk van de weegsensor."""

    def __init__(self):
        super().__init__(naam="KlWeegsensorMerk",
                         label="Weegsensor merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWeegsensorMerk",
                         definition="Het merk van de weegsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWeegsensorMerk")

        self.add_option("Kistler", "Kistler", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWeegsensorMerk/Kistler")
