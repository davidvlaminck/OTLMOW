# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoEcoductType(Keuzelijst):
    """Types van ecoduct."""

    def __init__(self):
        super().__init__(naam="KlEcoEcoductType",
                         label="Ecoduct type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoEcoductType",
                         definition="Types van ecoduct.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoEcoductType")

        self.add_option("ecoveloduct", "ecoveloduct", "Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met een fietspad.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecoveloduct")
        self.add_option("ecocreaduct", "ecocreaduct", "Een brug hoofdzakelijk in gebruik voor natuur, gecombineerd met zachte recreatie (fietsers, wandelaars, ruiters).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/ecocreaduct")
        self.add_option("bermbrug", "bermbrug", "Een bestaande, vaak smalle brug met beperkt verkeer waarop de natuur via groene bermen doorloopt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoEcoductType/bermbrug")
