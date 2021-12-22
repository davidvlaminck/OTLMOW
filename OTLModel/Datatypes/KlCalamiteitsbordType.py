from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCalamiteitsbordType(Keuzelijst):
    """Types van calamiteitsbord."""

    def __init__(self):
        super().__init__(naam="KlCalamiteitsbordType",
                         label="Calamiteitsbord type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCalamiteitsbordType",
                         definition="Types van calamiteitsbord.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCalamiteitsbordType")

        self.add_option("dragend-bord", "dragend bord", "Een dragend calamiteitsbord.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/dragend-bord")
        self.add_option("draaiend-bord", "draaiend bord", "Een draaiend calamiteitsbord.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCalamiteitsbordType/draaiend-bord")
