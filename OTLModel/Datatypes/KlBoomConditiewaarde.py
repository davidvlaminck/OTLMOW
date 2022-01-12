# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConditiewaarde(Keuzelijst):
    """De verschillende conditiewaardes voor een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomConditiewaarde",
                         label="Boom conditiewaarde",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConditiewaarde",
                         definition="De verschillende conditiewaardes voor een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConditiewaarde")

        self.add_option("0", "0", "Dode boom", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0")
        self.add_option("0.1", "0.1", "Bijna dode boom", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.1")
        self.add_option("0.2", "0.2", "kwijnende boom met zeer slechte conditie die binnen een periode van 2 jaar kan afsterven", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.2")
        self.add_option("0.3", "0.3", "kwijnende boom met zeer slechte conditie die binnen een periode van 3 jaar kan afsterven", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.3")
        self.add_option("0.4", "0.4", "kwijnende boom met een slechte conditie die binnen een periode van 4 jaar kan afsterven", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.4")
        self.add_option("0.5", "0.5", "kwijnende boom met een slechte conditie die binnen een periode van 5-6 jaar kan afsterven", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.5")
        self.add_option("0.6", "0.6", "Boom in matige conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF aanzienlijke schade of aantastingen aan stam, gesteltakken of wortels EN/OF matige levensverwachting.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.6")
        self.add_option("0.7", "0.7", "Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.7")
        self.add_option("0.8", "0.8", "Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.8")
        self.add_option("0.9", "0.9", "Boom in goede conditie voor zijn levensfase (bladbezetting, knopzetting, scheutlengte, kroonarchitectuur, …) EN/OF beperkte schade of aantastingen aan stam, gesteltakken of wortels EN/OF goede levensverwachting op middellange termijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/0.9")
        self.add_option("1.0", "1.0", "kerngezonde boom die voldoet aan alle vereisten wat gezondheid, levensverwachting, esthetisch aanzien en vormgeving betreft", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiewaarde/1.0")
