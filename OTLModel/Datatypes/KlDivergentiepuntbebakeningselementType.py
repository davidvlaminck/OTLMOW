from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDivergentiepuntbebakeningselementType(Keuzelijst):
    """De vormen van het divergentiepuntbebakeningselement."""

    def __init__(self):
        super().__init__(naam="KlDivergentiepuntbebakeningselementType",
                         label="Divergentiepuntbebakeningselementtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDivergentiepuntbebakeningselementType",
                         definition="De vormen van het divergentiepuntbebakeningselement.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDivergentiepuntbebakeningselementType")

        self.add_option("standaard-model", "standaard model", "Divergentiepuntbebakeningselement van 2 meter diameter (folie type 2).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/standaard-model")
        self.add_option("klein-model", "klein model", "Divergentiepuntbebakeningselement van 1 meter diameter (folie type 3.a).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDivergentiepuntbebakeningselementType/klein-model")
