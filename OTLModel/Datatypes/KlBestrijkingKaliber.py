# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestrijkingKaliber(Keuzelijst):
    """De mogelijke kalibers."""

    def __init__(self):
        super().__init__(naam="KlBestrijkingKaliber",
                         label="kalibers",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestrijkingKaliber",
                         definition="De mogelijke kalibers.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestrijkingKaliber")

        self.add_option("2-10", "2/10", "kaliber 2/10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-10")
        self.add_option("2-4", "2/4", "kaliber 2/4", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-4")
        self.add_option("2-6.3", "2/6.3", "kaliber 2/6.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/2-6.3")
        self.add_option("4-10", "4/10", "kaliber 4/10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-10")
        self.add_option("4-6.3", "4/6.3", "kaliber 4/6.3", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/4-6.3")
        self.add_option("6.3-10", "6.3/10", "kaliber 6.3/10", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestrijkingKaliber/6.3-10")
