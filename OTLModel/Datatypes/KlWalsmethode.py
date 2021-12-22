from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWalsmethode(Keuzelijst):
    """De manier waarop het staal is gewalst."""

    def __init__(self):
        super().__init__(naam="KlWalsmethode",
                         label="Walsmethode",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlWalsmethode",
                         definition="De manier waarop het staal is gewalst.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWalsmethode")

        self.add_option("koud", "Koud", "Staal die bij omgevingstemperatuur wordt gevormd (getrokken) uit warmgewalst staal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/koud")
        self.add_option("warm", "Warm", "Heet staal wordt vervormd onder druk van persen en walsen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWalsmethode/warm")
