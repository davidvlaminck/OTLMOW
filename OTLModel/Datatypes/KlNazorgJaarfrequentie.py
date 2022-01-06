# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNazorgJaarfrequentie(Keuzelijst):
    """Aantal keer dat jaarlijks de behandelde zone dient te worden gecontroleerd."""

    def __init__(self):
        super().__init__(naam="KlNazorgJaarfrequentie",
                         label="Nazorg jaarfrequentie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlNazorgJaarfrequentie",
                         definition="Aantal keer dat jaarlijks de behandelde zone dient te worden gecontroleerd.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNazorgJaarfrequentie")

        self.add_option("1", "1", "Nazorg wordt 1 keer per jaar uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/1")
        self.add_option("2", "2", "Nazorg wordt 2 keer per jaar uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/2")
        self.add_option("3", "3", "Nazorg wordt 3 keer per jaar uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/3")
        self.add_option("4", "4", "Nazorg wordt 4 keer per jaar uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNazorgJaarfrequentie/4")
