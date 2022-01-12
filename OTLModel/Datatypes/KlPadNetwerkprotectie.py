# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlPadNetwerkprotectie(Keuzelijst):
    """Lijst van referenties van paden die redundantie kunnen leveren aan een Pad."""

    def __init__(self):
        super().__init__(naam="KlPadNetwerkprotectie",
                         label="Pad netwerkprotectie",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlPadNetwerkprotectie",
                         definition="Lijst van referenties van paden die redundantie kunnen leveren aan een Pad.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPadNetwerkprotectie")

        self.add_option("Customer", "Customer", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Customer")
        self.add_option("LACP", "LACP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LACP")
        self.add_option("LCAS", "LCAS", "Link Capacity Adjustment Scheme (Enkel bij SDH)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/LCAS")
        self.add_option("MPLS-TP", "MPLS-TP", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MPLS-TP")
        self.add_option("MSSpring", "MSSpring", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/MSSpring")
        self.add_option("NULL", "NULL", "geen systeembeveiliging", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/NULL")
        self.add_option("None", "None", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/None")
        self.add_option("OPS", "OPS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/OPS")
        self.add_option("Other", "Other", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/Other")
        self.add_option("SNCP", "SNCP", "Sub Network Connection Protection (Bij OTN en SDH)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/SNCP")
        self.add_option("STP", "STP", "Carrier Ethernet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPadNetwerkprotectie/STP")
