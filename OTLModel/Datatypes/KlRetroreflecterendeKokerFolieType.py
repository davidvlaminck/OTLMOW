# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRetroreflecterendeKokerFolieType(Keuzelijst):
    """Keuzeijst voor het bepalen van folietype van de retroreflecterende koker."""

    def __init__(self):
        super().__init__(naam="KlRetroreflecterendeKokerFolieType",
                         label="Retroreflecterende koker folie type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendeKokerFolieType",
                         definition="Keuzeijst voor het bepalen van folietype van de retroreflecterende koker.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendeKokerFolieType")

        self.add_option("type-2", "type 2", "Keuze folie type 2 (geel) als folietype van de retroreflecterende koker", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-2")
        self.add_option("type-3", "type 3", "Keuze folie type 3 als folietype (geel - fluorescerend) van de retroreflecterende koker", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendeKokerFolieType/type-3")
