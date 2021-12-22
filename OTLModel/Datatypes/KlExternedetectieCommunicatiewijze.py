from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlExternedetectieCommunicatiewijze(Keuzelijst):
    """Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar."""

    def __init__(self):
        super().__init__(naam="KlExternedetectieCommunicatiewijze",
                         label="Externedetectie communicatiewijze",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieCommunicatiewijze",
                         definition="Keuzelijst met de verschillende manieren waarop een externe detectie communiceert met een verkeersregelaar.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieCommunicatiewijze")

        self.add_option("serieel", "serieel", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/serieel")
        self.add_option("protocol", "protocol", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/protocol")
        self.add_option("contact", "contact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieCommunicatiewijze/contact")
