# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgWeekdagen(Keuzelijst):
    """Lijst van de verschillende weekdagen."""

    def __init__(self):
        super().__init__(naam="KlAlgWeekdagen",
                         label="Weekdagen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgWeekdagen",
                         definition="Lijst van de verschillende weekdagen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgWeekdagen")

        self.add_option("maandag", "maandag", "De dag van een week tussen zondag en dinsdag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/maandag")
        self.add_option("dinsdag", "dinsdag", "De dag van een week tussen maandag en woensdag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/dinsdag")
        self.add_option("woensdag", "woensdag", "De dag van een week tussen dinsdag en donderdag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/woensdag")
        self.add_option("donderdag", "donderdag", "De dag van een week tussen woensdag en vrijdag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/donderdag")
        self.add_option("vrijdag", "vrijdag", "De dag van een week tussen donderdag en zaterdag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/vrijdag")
        self.add_option("zaterdag", "zaterdag", "De dag van een week tussen vrijdag en zondag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zaterdag")
        self.add_option("zondag", "zondag", "De dag van een week tussen zaterdag en maandag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/zondag")
        self.add_option("feestdag", "feestdag", "Een wettelijke nationale vrije dag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgWeekdagen/feestdag")
