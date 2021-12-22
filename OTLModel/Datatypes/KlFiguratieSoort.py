from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlFiguratieSoort(Keuzelijst):
    """Soorten van figuratie markering."""

    def __init__(self):
        super().__init__(naam="KlFiguratieSoort",
                         label="Figuratie soort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieSoort",
                         definition="Soorten van figuratie markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieSoort")

        self.add_option("aanduiding-bebouwde-kom-met-blokken", "aanduiding bebouwde kom met blokken", "Aanduiding bebouwde kom met blokken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/aanduiding-bebouwde-kom-met-blokken")
        self.add_option("aanduiding-bebouwde-kom---snelheidsbeperking-(50)", "aanduiding bebouwde kom - snelheidsbeperking (50)", "Aanduiding bebouwde kom met blokken met snelheidsbeperking van 50 (zonder cirkel).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/aanduiding-bebouwde-kom---snelheidsbeperking-(50)")
        self.add_option("pijl", "pijl", "Een pijlvormige markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/pijl")
        self.add_option("letterfiguratiemarkering", "letterfiguratiemarkering", "Een lettermarking als figuratie zoals BUS, TAXI, TRAM,....", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/letterfiguratiemarkering")
        self.add_option("bushalte-met-arcering", "bushalte met arcering", "Een lettermarkering BUS met arcering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/bushalte-met-arcering")
        self.add_option("bushalte-zonder-arcering", "bushalte zonder arcering", "Een lettermarkering BUS zonder arcering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/bushalte-zonder-arcering")
        self.add_option("verkeersbord", "verkeersbord", "Een markering in de vorm van een verkeersbord.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/verkeersbord")
        self.add_option("logo", "logo", "Een markering in de vorm van een logo.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/logo")
        self.add_option("visgraatmarkering", "visgraatmarkering", "Een visgraatmarkering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/visgraatmarkering")
        self.add_option("hm", "hm", "Referentiepuntmarkering hectometer- en kilometeraanduiding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/hm")
        self.add_option("omgekeerde-driehoek", "omgekeerde driehoek", "Een omgekeerde driehoek markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoort/omgekeerde-driehoek")
