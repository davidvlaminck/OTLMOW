from OTLModel.Datatypes.Keuzelijst import Keuzelijst


class KlMaaiPeriode(Keuzelijst):
    def __init__(self):
        super().__init__(naam="KlMaaiPeriode",
                         label="Maai Periode",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlMaaiPeriode",
                         definition="Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiPeriode")
