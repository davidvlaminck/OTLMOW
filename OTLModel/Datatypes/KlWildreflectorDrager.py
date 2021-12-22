from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWildreflectorDrager(Keuzelijst):
    """Mogelijke dragers van een wildreflector."""

    def __init__(self):
        super().__init__(naam="KlWildreflectorDrager",
                         label="Wildreflector drager",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWildreflectorDrager",
                         definition="Mogelijke dragers van een wildreflector.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWildreflectorDrager")

        self.add_option("houten-paal", "houten paal", "houten paal als drager.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/houten-paal")
        self.add_option("metalen-paal", "metalen paal", "metalen paal als drager.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWildreflectorDrager/metalen-paal")
