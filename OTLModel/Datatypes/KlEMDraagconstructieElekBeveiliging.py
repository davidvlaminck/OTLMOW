from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlEMDraagconstructieElekBeveiliging(Keuzelijst):
    """Type elektrische beveiliging aanwezig in de draagconstructie."""

    def __init__(self):
        super().__init__(naam="KlEMDraagconstructieElekBeveiliging",
                         label="EM-draagconstructie elektrische beveiliging",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEMDraagconstructieElekBeveiliging",
                         definition="Type elektrische beveiliging aanwezig in de draagconstructie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEMDraagconstructieElekBeveiliging")

        self.add_option("automaat", "automaat", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/automaat")
        self.add_option("smeltzekering", "smeltzekering", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/smeltzekering")
        self.add_option("differentieelautomaat", "differentieelautomaat", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/differentieelautomaat")
