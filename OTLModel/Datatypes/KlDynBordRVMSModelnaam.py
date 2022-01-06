# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSModelnaam(Keuzelijst):
    """Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald."""

    def __init__(self):
        super().__init__(naam="KlDynBordRVMSModelnaam",
                         label="Dyn bord RVMS modelnaam",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSModelnaam",
                         definition="Keuzelijst met de gangbare modelnamen van RVMS borden. De modelnamen worden meestal door de leverancier of fabrikant bepaald.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSModelnaam")

        self.add_option("RVMS-06I04", "RVMS-06I04", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-06I04")
        self.add_option("RVMS-12F05", "RVMS-12F05", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordRVMSModelnaam/RVMS-12F05")
