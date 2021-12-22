from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBoomPlantwijzewaarde(Keuzelijst):
    """De verschillende opties van de plantwijzewaarde."""

    def __init__(self):
        super().__init__(naam="KlBoomPlantwijzewaarde",
                         label="Boom plantwijzewaarde",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomPlantwijzewaarde",
                         definition="De verschillende opties van de plantwijzewaarde.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomPlantwijzewaarde")

        self.add_option("1", "1", "solitaire plant", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/1")
        self.add_option("0.8", "0.8", "rijbeplanting met belangrijke uitval", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.8")
        self.add_option("0.6", "0.6", "boom in groep van 6 - 10 stuks", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.6")
        self.add_option("0.4", "0.4", "boom in grote dicht beplante groepen (> 10 stuks) (ook bosachtige beplantingen, bospark)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.4")
        self.add_option("0.7", "0.7", "boom in groep van 2 - 5 stuks", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.7")
        self.add_option("0.9", "0.9", "perfecte rijbeplanting (zonder uitval)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomPlantwijzewaarde/0.9")
