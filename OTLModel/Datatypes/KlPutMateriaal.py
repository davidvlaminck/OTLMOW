from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlPutMateriaal(Keuzelijst):
    """Vervaardigingsmaterialen van de put."""

    def __init__(self):
        super().__init__(naam="KlPutMateriaal",
                         label="Put materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPutMateriaal",
                         definition="Vervaardigingsmaterialen van de put.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPutMateriaal")

        self.add_option("beton-of-gres", "beton of gres", "beton of gres", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-gres")
        self.add_option("glasvezelversterkt-polyesterhars", "glasvezelversterkt polyesterhars", "glasvezelversterkt polyesterhars", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/glasvezelversterkt-polyesterhars")
        self.add_option("ter-plaatse-gestort-beton", "ter plaatse gestort beton", "ter plaatse gestort beton", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/ter-plaatse-gestort-beton")
        self.add_option("beton-of-metselwerk", "beton of metselwerk", "beton of metselwerk", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/beton-of-metselwerk")
        self.add_option("PE-of-PP", "PE of PP", "PE of PP", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPutMateriaal/PE-of-PP")
