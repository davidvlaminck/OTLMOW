from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlGeleidingMateriaal(Keuzelijst):
    """Materialen voor de geleidingwand om kleinere wilde dieren te geleiden."""

    def __init__(self):
        super().__init__(naam="KlGeleidingMateriaal",
                         label="Geleiding materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGeleidingMateriaal",
                         definition="Materialen voor de geleidingwand om kleinere wilde dieren te geleiden.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGeleidingMateriaal")

        self.add_option("beton", "beton", "Geleiding bestaande uit een betonnen wand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/beton")
        self.add_option("kunststof", "kunststof", "Geleiding bestaande uit een kunststoffen wand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/kunststof")
        self.add_option("metaal", "metaal", "Geleiding bestaande uit een metalen wand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGeleidingMateriaal/metaal")
