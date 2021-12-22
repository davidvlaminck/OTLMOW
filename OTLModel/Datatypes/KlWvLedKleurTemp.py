from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLedKleurTemp(Keuzelijst):
    """Kleurtemperatuur van de LED's."""

    def __init__(self):
        super().__init__(naam="KlWvLedKleurTemp",
                         label="WV LED kleurtemperatuur",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLedKleurTemp",
                         definition="Kleurtemperatuur van de LED's.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLedKleurTemp")

        self.add_option("2900", "2900", "/ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/2900")
        self.add_option("4000", "4000", "/ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/4000")
        self.add_option("1700", "1700", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLedKleurTemp/1700")
