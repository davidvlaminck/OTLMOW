# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEnergiemeterDNBUurtarief(Keuzelijst):
    """Type uurtarief vb enkelvoudig, dubbelvoudig,..."""

    def __init__(self):
        super().__init__(naam="KlEnergiemeterDNBUurtarief",
                         label="Energiemeter DNB uurtarief",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEnergiemeterDNBUurtarief",
                         definition="Type uurtarief vb enkelvoudig, dubbelvoudig,...",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEnergiemeterDNBUurtarief")

        self.add_option("enkelvoudig", "enkelvoudig", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/enkelvoudig")
        self.add_option("dubbelvoudig", "dubbelvoudig", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/dubbelvoudig")
        self.add_option("dubbelvoudig-maar-enkelvoudig-gebruikt", "dubbelvoudig maar enkelvoudig gebruikt", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEnergiemeterDNBUurtarief/dubbelvoudig-maar-enkelvoudig-gebruikt")
