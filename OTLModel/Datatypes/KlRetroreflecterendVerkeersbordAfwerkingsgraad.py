from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlRetroreflecterendVerkeersbordAfwerkingsgraad(Keuzelijst):
    """Keuzeopties om de afwerkingsgraad van een RetroreflecterendVerkeersbord aan te geven volgens SB250."""

    def __init__(self):
        super().__init__(naam="KlRetroreflecterendVerkeersbordAfwerkingsgraad",
                         label="Keuzelijst afwerkingsgraad retroreflecterend verkeersbord",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRetroreflecterendVerkeersbordAfwerkingsgraad",
                         definition="Keuzeopties om de afwerkingsgraad van een RetroreflecterendVerkeersbord aan te geven volgens SB250.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRetroreflecterendVerkeersbordAfwerkingsgraad")

        self.add_option("zonder-tekst.-symbool-of-overlay", "zonder tekst, symbool of overlay", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordAfwerkingsgraad/zonder-tekst.-symbool-of-overlay")
        self.add_option("volledig-afgewerkt", "volledig afgewerkt", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRetroreflecterendVerkeersbordAfwerkingsgraad/volledig-afgewerkt")
