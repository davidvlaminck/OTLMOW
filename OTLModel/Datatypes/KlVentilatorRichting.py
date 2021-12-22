from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVentilatorRichting(Keuzelijst):
    """Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden."""

    def __init__(self):
        super().__init__(naam="KlVentilatorRichting",
                         label="Ventilator richting",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorRichting",
                         definition="Keuzelijst die aangeeft of de luchtstroom in één richting of beide richtingen kan plaatsvinden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorRichting")

        self.add_option("unidirectioneel", "unidirectioneel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/unidirectioneel")
        self.add_option("bidirectioneel", "bidirectioneel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorRichting/bidirectioneel")
