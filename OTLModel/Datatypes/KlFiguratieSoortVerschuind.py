from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlFiguratieSoortVerschuind(Keuzelijst):
    """Soorten van verschuinde figuratie markering."""

    def __init__(self):
        super().__init__(naam="KlFiguratieSoortVerschuind",
                         label="Figuratie soort verschuind",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieSoortVerschuind",
                         definition="Soorten van verschuinde figuratie markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieSoortVerschuind")

        self.add_option("letterfiguratiemarkering(schuin)", "letterfiguratiemarkering(schuin)", "Een schuine lettermarking als figuratie zoals BUS, TAXI, TRAM,....", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/letterfiguratiemarkering(schuin)")
        self.add_option("omgekeerde-driehoek(schuin)", "omgekeerde driehoek(schuin)", "Een schuine omgekeerde driehoek markering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieSoortVerschuind/omgekeerde-driehoek(schuin)")
