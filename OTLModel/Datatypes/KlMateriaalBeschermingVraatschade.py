from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlMateriaalBeschermingVraatschade(Keuzelijst):
    """De middelen als bescherming tegen vraatschade."""

    def __init__(self):
        super().__init__(naam="KlMateriaalBeschermingVraatschade",
                         label="Materiaal bescherming vraatschade",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMateriaalBeschermingVraatschade",
                         definition="De middelen als bescherming tegen vraatschade.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMateriaalBeschermingVraatschade")

        self.add_option("wildafwerend-product", "wildafwerend product", "Wildafwerend product wordt gebruikt als bescherming tegen vraatschade.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/wildafwerend-product")
        self.add_option("kunststof", "kunststof", "Materiaal dat gebruikt wordt als bescherming vraatschade is kunststof.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/kunststof")
        self.add_option("juteband", "juteband", "Materiaal dat gebruikt wordt als bescherming vraatschade is een juteband.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMateriaalBeschermingVraatschade/juteband")
