# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOmegaElementMateriaal(Keuzelijst):
    """De gebruikte materialen van het omega-element."""

    def __init__(self):
        super().__init__(naam="KlOmegaElementMateriaal",
                         label="Omega element materiaal",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOmegaElementMateriaal",
                         definition="De gebruikte materialen van het omega-element.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOmegaElementMateriaal")

        self.add_option("aluminium", "aluminium", "Omega-element vervaarigd uit aluminium.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/aluminium")
        self.add_option("roestvrij-staal", "roestvrij staal", "Omega-element vervaarigd uit roestvrij staal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/roestvrij-staal")
        self.add_option("verzinkt-staal", "verzinkt staal", "Omega-element vervaarigd uit verzinkt staal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmegaElementMateriaal/verzinkt-staal")
