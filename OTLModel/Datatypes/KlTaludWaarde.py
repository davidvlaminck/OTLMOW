# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTaludWaarde(Keuzelijst):
    """De verschillende mogelijke waardes voor de hellingsgraad van de talud."""

    def __init__(self):
        super().__init__(naam="KlTaludWaarde",
                         label="Talud waarde",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTaludWaarde",
                         definition="De verschillende mogelijke waardes voor de hellingsgraad van de talud.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTaludWaarde")

        self.add_option("tot-1-3", "tot 1 3", "Een hellingsgraad tot 1/3 (33,33%, 18,4°).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/tot-1-3")
        self.add_option("van-1-1-en-steiler", "van 1 1 en steiler", "Hellingsgraad van 1/1 (100%, 45°) of steiler.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-1-en-steiler")
        self.add_option("van-1-2-tot-1-1", "van 1 2 tot 1 1", "Een hellingsgraad van 1/2 (50%, 26,6%) tot 1/1 (100%, 45°).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-2-tot-1-1")
        self.add_option("van-1-3-tot-1-2", "van 1 3 tot 1 2", "Een hellingsgraad van 1/3 (33,33%, 18,4°) tot 1/2 (50%, 26,6°).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludWaarde/van-1-3-tot-1-2")
