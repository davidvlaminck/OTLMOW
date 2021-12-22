from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlOntvangerMerk(Keuzelijst):
    """Keuzelijst met merknamen voor Ontvanger."""

    def __init__(self):
        super().__init__(naam="KlOntvangerMerk",
                         label="ontvanger merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOntvangerMerk",
                         definition="Keuzelijst met merknamen voor Ontvanger.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOntvangerMerk")

