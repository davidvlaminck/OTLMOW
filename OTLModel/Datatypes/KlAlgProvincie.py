from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlAlgProvincie(Keuzelijst):
    """Lijst van provincies in Vlaanderen."""

    def __init__(self):
        super().__init__(naam="KlAlgProvincie",
                         label="Provincie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgProvincie",
                         definition="Lijst van provincies in Vlaanderen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgProvincie")

        self.add_option("antwerpen", "antwerpen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/antwerpen")
        self.add_option("limburg", "limburg", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/limburg")
        self.add_option("oost-Vlaanderen", "oost-Vlaanderen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/oost-Vlaanderen")
        self.add_option("vlaams-Brabant", "vlaams-Brabant", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/vlaams-Brabant")
        self.add_option("west-Vlaanderen", "west-Vlaanderen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgProvincie/west-Vlaanderen")
