from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVriTypeweggebruiker(Keuzelijst):
    """Lijst met types van weggebruikers."""

    def __init__(self):
        super().__init__(naam="KlVriTypeweggebruiker",
                         label="VRI detector typeweggebruiker",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVriTypeweggebruiker",
                         definition="Lijst met types van weggebruikers.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriTypeweggebruiker")

        self.add_option("voertuig", "voertuig", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/voertuig")
        self.add_option("bus", "bus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/bus")
        self.add_option("fiets", "fiets", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/fiets")
        self.add_option("voetganger", "voetganger", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/voetganger")
        self.add_option("tram", "tram", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/tram")
        self.add_option("vrachtwagen", "vrachtwagen", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriTypeweggebruiker/vrachtwagen")
