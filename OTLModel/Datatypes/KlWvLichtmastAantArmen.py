from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWvLichtmastAantArmen(Keuzelijst):
    """Aantal armen van de lichtmast."""

    def __init__(self):
        super().__init__(naam="KlWvLichtmastAantArmen",
                         label="WV-mast aantal armen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastAantArmen",
                         definition="Aantal armen van de lichtmast.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastAantArmen")

        self.add_option("0", "0", "keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/0")
        self.add_option("1", "1", "keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/1")
        self.add_option("2", "2", "keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/2")
        self.add_option("3", "3", "keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/3")
        self.add_option("4", "4", "keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/4")
