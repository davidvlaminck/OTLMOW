# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlIORichting(Keuzelijst):
    """Geeft aan of de IO-kaart dient voor input of output."""

    def __init__(self):
        super().__init__(naam="KlIORichting",
                         label="IO richting",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIORichting",
                         definition="Geeft aan of de IO-kaart dient voor input of output.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIORichting")

        self.add_option("input", "input", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/input")
        self.add_option("output", "output", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIORichting/output")
