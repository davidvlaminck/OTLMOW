from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlZpadType(Keuzelijst):
    """De soort verbinding, gebaseerd op het gebruikte protocol."""

    def __init__(self):
        super().__init__(naam="KlZpadType",
                         label="Z-pad type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlZpadType",
                         definition="De soort verbinding, gebaseerd op het gebruikte protocol.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZpadType")

        self.add_option("Ethernet", "Ethernet", "Packet switched netwerkstandaard waarmee computers in een LAN met elkaar communiceren, via het MEF metro ethernet forum wordt gebruikte apparatuur gecertificeerd tegen de ethernet standaarden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/Ethernet")
        self.add_option("FC", "FC", "Fibre Channel protocol, standaard, gebruikt voor Storage Area Netwerken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/FC")
        self.add_option("E1", "E1", "E1 signaal is een TDM signaal van 2Mb/s, verdeeld in 64 kbit/s kanalen, vooral gebruikt voor telefonie en lage snelheid data transmissie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/E1")
        self.add_option("Other", "Other", "Ander soort verbinding", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/Other")
        self.add_option("NULL", "NULL", "niet ingevuld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlZpadType/NULL")
