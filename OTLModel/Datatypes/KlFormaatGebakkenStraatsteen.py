from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlFormaatGebakkenStraatsteen(Keuzelijst):
    """De formaten van gebakken straatsteen."""

    def __init__(self):
        super().__init__(naam="KlFormaatGebakkenStraatsteen",
                         label="Formaat gebakken straatsteen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFormaatGebakkenStraatsteen",
                         definition="De formaten van gebakken straatsteen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFormaatGebakkenStraatsteen")

        self.add_option("dikformaat-(ca.-200-x-ca.-65-mm)", "dikformaat (ca. 200 x ca. 65 mm)", "Een gestandaardiseerde maat voor de gebakken straatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/dikformaat-(ca.-200-x-ca.-65-mm)")
        self.add_option("keiformaat-(ca.-200-x-ca.-100-mm)", "keiformaat (ca. 200 x ca. 100 mm)", "Een gestandaardiseerde maat voor de gebakken straatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/keiformaat-(ca.-200-x-ca.-100-mm)")
        self.add_option("rijnformaat-(ca.-180-x-ca.-45-mm)", "rijnformaat (ca. 180 x ca. 45 mm)", "Een gestandaardiseerde maat voor de gebakken straatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/rijnformaat-(ca.-180-x-ca.-45-mm)")
        self.add_option("langformaat-(ca.-240-x-ca.-80-mm)", "langformaat (ca. 240 x ca. 80 mm)", "Een gestandaardiseerde maat voor de gebakken straatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/langformaat-(ca.-240-x-ca.-80-mm)")
        self.add_option("waalformaat-(ca.-200-x-ca.-50-mm)", "waalformaat (ca. 200 x ca. 50 mm)", "Een gestandaardiseerde maat voor de gebakken straatsteen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/waalformaat-(ca.-200-x-ca.-50-mm)")
