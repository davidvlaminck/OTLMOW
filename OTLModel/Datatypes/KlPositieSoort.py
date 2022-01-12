# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPositieSoort(Keuzelijst):
    """Posities van het wegdek."""

    def __init__(self):
        super().__init__(naam="KlPositieSoort",
                         label="Positie soort",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPositieSoort",
                         definition="Posities van het wegdek.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPositieSoort")

        self.add_option("linkerrand", "linkerrand", "linkerrand", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/linkerrand")
        self.add_option("midden", "midden", "midden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/midden")
        self.add_option("rechterrand", "rechterrand", "rechterrand", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPositieSoort/rechterrand")
