from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBestratingAfwerking(Keuzelijst):
    """De manieren van afwerking van de bestrating."""

    def __init__(self):
        super().__init__(naam="KlBestratingAfwerking",
                         label="Bestrating afwerking",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingAfwerking",
                         definition="De manieren van afwerking van de bestrating.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingAfwerking")

        self.add_option("gezaagd", "gezaagd", "gezaagd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gezaagd")
        self.add_option("onbehandeld", "onbehandeld", "onbehandeld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/onbehandeld")
        self.add_option("poreus", "poreus", "poreus", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/poreus")
        self.add_option("getrommeld", "getrommeld", "getrommeld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/getrommeld")
        self.add_option("geschuurd", "geschuurd", "geschuurd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geschuurd")
        self.add_option("gestaaldstraald", "gestaaldstraald", "gestaaldstraald", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gestaaldstraald")
        self.add_option("gewassen", "gewassen", "gewassen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gewassen")
        self.add_option("geslepen", "geslepen", "geslepen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geslepen")
        self.add_option("gezandstraald", "gezandstraald", "gezandstraald", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gezandstraald")
        self.add_option("gebouchardeerd", "gebouchardeerd", "gebouchardeerd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gebouchardeerd")
        self.add_option("geslepen-en-gestraald", "geslepen en gestraald", "geslepen en gestraald", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/geslepen-en-gestraald")
        self.add_option("gevlamd", "gevlamd", "gevlamd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gevlamd")
        self.add_option("gekliefd", "gekliefd", "gekliefd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gekliefd")
        self.add_option("gefrijnd", "gefrijnd", "gefrijnd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gefrijnd")
        self.add_option("gehamerd", "gehamerd", "gehamerd", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/gehamerd")
        self.add_option("afwerking-volgens-de-opdrachtdocumenten", "afwerking volgens de opdrachtdocumenten", "afwerking volgens de opdrachtdocumenten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingAfwerking/afwerking-volgens-de-opdrachtdocumenten")
