from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDraagConstrBeschermlaag(Keuzelijst):
    """De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming."""

    def __init__(self):
        super().__init__(naam="KlDraagConstrBeschermlaag",
                         label="Draagconstructie beschermlaag",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagConstrBeschermlaag",
                         definition="De manieren van aanbrengen van een beschermlaag ter voorkoming van roestvorming.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDraagConstrBeschermlaag")

        self.add_option("gegalvaniseerd", "gegalvaniseerd", "Een laag zink aangebracht om roest te voorkomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gegalvaniseerd")
        self.add_option("gecoat", "gecoat", "Een mengsel van stoffen aangebracht om roest te voorkomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/gecoat")
        self.add_option("geschilderd", "geschilderd", "Een laag verf aangebracht om roest te voorkomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDraagConstrBeschermlaag/geschilderd")
