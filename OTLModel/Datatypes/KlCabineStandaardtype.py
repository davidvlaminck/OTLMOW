from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlCabineStandaardtype(Keuzelijst):
    """Veel voorkomende types van cabines."""

    def __init__(self):
        super().__init__(naam="KlCabineStandaardtype",
                         label="Cabine standaardtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCabineStandaardtype",
                         definition="Veel voorkomende types van cabines.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCabineStandaardtype")

        self.add_option("lokaal-in-een-gebouw", "lokaal in een gebouw", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/lokaal-in-een-gebouw")
        self.add_option("gemetst-betreedbaar", "gemetst betreedbaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/gemetst-betreedbaar")
        self.add_option("aluminium-niet-betreedbaar", "aluminium niet betreedbaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-niet-betreedbaar")
        self.add_option("aluminium-betreedbaar", "aluminium betreedbaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/aluminium-betreedbaar")
        self.add_option("beton-niet-betreedbaar-(compactstation)", "beton niet betreedbaar (compactstation)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-niet-betreedbaar-(compactstation)")
        self.add_option("beton-betreedbaar", "beton betreedbaar", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCabineStandaardtype/beton-betreedbaar")
