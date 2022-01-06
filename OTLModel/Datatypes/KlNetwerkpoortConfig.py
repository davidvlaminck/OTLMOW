# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortConfig(Keuzelijst):
    """Lijst van mogelijke soort verbindingen aangeboden aan de klant van Netwerkpoorten."""

    def __init__(self):
        super().__init__(naam="KlNetwerkpoortConfig",
                         label="Netwerkpoort configuratie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortConfig",
                         definition="Lijst van mogelijke soort verbindingen aangeboden aan de klant van Netwerkpoorten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortConfig")

        self.add_option("STM-1", "STM-1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-1")
        self.add_option("STM-4", "STM-4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-4")
        self.add_option("STM-16", "STM-16", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-16")
        self.add_option("STM-64", "STM-64", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-64")
        self.add_option("OTU-1", "OTU-1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-1")
        self.add_option("OTU-2", "OTU-2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-2")
        self.add_option("OTU-4", "OTU-4", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/OTU-4")
        self.add_option("E1", "E1", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/E1")
        self.add_option("E", "E", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/E")
        self.add_option("40GE", "40GE", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/40GE")
        self.add_option("FE", "FE", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/FE")
        self.add_option("GE", "GE", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/GE")
        self.add_option("10GE", "10GE", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/10GE")
        self.add_option("100GE", "100GE", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/100GE")
        self.add_option("1G-FC", "1G FC", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/1G-FC")
        self.add_option("4G-FC", "4G FC", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/4G-FC")
        self.add_option("8G-FC", "8G FC", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/8G-FC")
        self.add_option("16G-FC", "16G FC", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/16G-FC")
        self.add_option("Other", "Other", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/Other")
        self.add_option("NULL", "NULL", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/NULL")
