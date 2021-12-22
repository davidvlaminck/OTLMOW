from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlDynBordVMSModelnaam(Keuzelijst):
    """Keuzelijst met de gangbare modelnamen van VMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""

    def __init__(self):
        super().__init__(naam="KlDynBordVMSModelnaam",
                         label="Dyn bord VMS modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordVMSModelnaam",
                         definition="Keuzelijst met de gangbare modelnamen van VMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordVMSModelnaam")

        self.add_option("VMS-00A09", "VMS-00A09", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-00A09")
        self.add_option("VMS-07J06", "VMS-07J06", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-07J06")
        self.add_option("VMS-10G01", "VMS-10G01", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordVMSModelnaam/VMS-10G01")
