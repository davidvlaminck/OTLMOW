from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlIVRIModelTLCfi(Keuzelijst):
    """De modelnaam van de TLC-fi poort."""

    def __init__(self):
        super().__init__(naam="KlIVRIModelTLCfi",
                         label="iVRIModelTLCfi",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlIVRIModelTLCfi",
                         definition="De modelnaam van de TLC-fi poort.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlIVRIModelTLCfi")

        self.add_option("civa-2020", "CIVA 2020", "CIVA 2020", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/civa-2020")
        self.add_option("flownode", "FlowNode", "FlowNode", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/flownode")
        self.add_option("tlc-fi-broker", "TLC-FI broker", "TLC-FI broker", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlIVRIModelTLCfi/tlc-fi-broker")
