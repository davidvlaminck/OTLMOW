from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBeschermingMaaischade(Keuzelijst):
    """De middelen als bescherming tegen maaischade."""

    def __init__(self):
        super().__init__(naam="KlBeschermingMaaischade",
                         label="Bescherming maaischade",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBeschermingMaaischade",
                         definition="De middelen als bescherming tegen maaischade.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeschermingMaaischade")

        self.add_option("kunststof", "kunststof", "Bescherming in kunststof.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/kunststof")
        self.add_option("houten-paal", "houten paal", "Bescherming dmv een houten paal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeschermingMaaischade/houten-paal")
