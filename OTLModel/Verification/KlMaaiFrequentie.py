from OTLModel.Datatypes.KeuzelijstField import Keuzelijst


class KlMaaiFrequentie(Keuzelijst):
    def __init__(self):
        super().__init__(naam="KlMaaiFrequentie",
                         label="Maai Frequentie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlMaaiFrequentie",
                         definition="Keuzelijst met fasen uit de levenscyclus van een object om de toestand op een moment mee vast te leggen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiFrequentie")
