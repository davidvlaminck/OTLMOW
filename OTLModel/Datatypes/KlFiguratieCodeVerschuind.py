from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlFiguratieCodeVerschuind(Keuzelijst):
    """Codes voor de verschuinde figuratie markering."""

    def __init__(self):
        super().__init__(naam="KlFiguratieCodeVerschuind",
                         label="Figuratie code verschuind",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieCodeVerschuind",
                         definition="Codes voor de verschuinde figuratie markering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieCodeVerschuind")

        self.add_option("STOP-SmSc", "STOP-SmSc", "Een STOP markering smal en schuin.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/STOP-SmSc")
        self.add_option("VB-B1-GRsch", "VB-B1-GRsch", "Een omgekeerde driehoekmarkering groot en schuin.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieCodeVerschuind/VB-B1-GRsch")
