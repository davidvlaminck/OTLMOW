# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSelLusSoort(Keuzelijst):
    """Keuzelijst met verschillende soorten selectieve lussen."""

    def __init__(self):
        super().__init__(naam="KlSelLusSoort",
                         label="Selectieve lus soort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSelLusSoort",
                         definition="Keuzelijst met verschillende soorten selectieve lussen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSelLusSoort")

        self.add_option("buslus", "buslus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/buslus")
        self.add_option("tramlus", "tramlus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus")
        self.add_option("trambuslus", "trambuslus", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus")
        self.add_option("tramlus-magnetisch", "tramlus magnetisch", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-magnetisch")
        self.add_option("tramlus-wisselcontact-DeLijn", "tramlus wisselcontact DeLijn", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-wisselcontact-DeLijn")
        self.add_option("tramlus-virtueel", "tramlus virtueel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/tramlus-virtueel")
        self.add_option("trambuslus-virtueel", "trambuslus virtueel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSelLusSoort/trambuslus-virtueel")
