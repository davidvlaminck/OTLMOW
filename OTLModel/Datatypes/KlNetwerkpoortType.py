# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkpoortType(Keuzelijst):
    """Lijst van types voor Netwerkpoort."""

    def __init__(self):
        super().__init__(naam="KlNetwerkpoortType",
                         label="Netwerkpoort type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkpoortType",
                         definition="Lijst van types voor Netwerkpoort.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkpoortType")

        self.add_option("UNI", "UNI", "User-Network-Interface: deze poort verbindt het netwerk toestel met de poort van een gebruiker.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/UNI")
        self.add_option("NNI", "NNI", "Network-Network-Interface: deze poort verbindt het netwerk toestel met een poort van een ander netwerk toestel.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NNI")
        self.add_option("Other", "Other", "Ander, onbekend type interface.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/Other")
        self.add_option("NULL", "NULL", "Geen interface.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/NULL")
