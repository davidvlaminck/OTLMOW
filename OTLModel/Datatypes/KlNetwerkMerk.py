from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlNetwerkMerk(Keuzelijst):
    """Merknamen voor Netwerkelementen."""

    def __init__(self):
        super().__init__(naam="KlNetwerkMerk",
                         label="Netwerkelement merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkMerk",
                         definition="Merknamen voor Netwerkelementen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkMerk")

        self.add_option("NOKIA", "NOKIA", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA")
        self.add_option("Ciena", "Ciena", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena")
        self.add_option("Cisco", "Cisco", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Cisco")
        self.add_option("HP", "HP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/HP")
        self.add_option("Proxim", "Proxim", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Proxim")
        self.add_option("ABB", "ABB", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/ABB")
        self.add_option("Other", "Other", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Other")
        self.add_option("NULL", "NULL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NULL")
