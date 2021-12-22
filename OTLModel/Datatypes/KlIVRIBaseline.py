from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlIVRIBaseline(Keuzelijst):
    """De specificatieversie van het protocol van de iVRI component."""

    def __init__(self):
        super().__init__(naam="KlIVRIBaseline",
                         label="iVRIBaseline",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlIVRIBaseline",
                         definition="De specificatieversie van het protocol van de iVRI component.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIBaseline")

        self.add_option("idd-tlc-fi-version-1-3-1", "IDD TLC-FI version 1.3.1", "IDD TLC-FI version 1.3.1", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIBaseline/idd-tlc-fi-version-1-3-1")
