# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHardwareCdDvdTape import KlHardwareCdDvdTape
from OTLModel.Datatypes.KlHardwareDomein import KlHardwareDomein
from OTLModel.Datatypes.KlHardwareOS import KlHardwareOS
from OTLModel.Datatypes.KwantWrdInGigabyte import KwantWrdInGigabyte
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class HardwareToegang(AIMNaamObject):
    """Een abstracte die de gemeenschappelijke kenmerken bevat voor zowel fysieke als virtuele hardware."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.cdDvdTape = KeuzelijstField(naam="cdDvdTape",
                                         label="CD DVD Tape",
                                         lijst=KlHardwareCdDvdTape(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.cdDvdTape",
                                         definition="De hardware uitgerust met CD/DVD/Tape.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De hardware uitgerust met CD/DVD/Tape."""

        self.CPU = StringField(naam="CPU",
                               label="CPU",
                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.CPU",
                               definition="Centrale verwerkingseenheid.",
                               constraints="",
                               usagenote="",
                               deprecated_version="")
        """Centrale verwerkingseenheid."""

        self.disk = KwantWrdInGigabyte()
        """De disk config van de hardware, HD, RAID, ..."""
        self.disk.naam = "disk"
        self.disk.label = "disk"
        self.disk.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.disk"
        self.disk.definition = "De disk config van de hardware, HD, RAID, ..."
        self.disk.constraints = ""
        self.disk.usagenote = ""
        self.disk.deprecated_version = ""

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.domein = KeuzelijstField(naam="domein",
                                      label="domein",
                                      lijst=KlHardwareDomein(),
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.domein",
                                      definition="Administratieve groepering van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Administratieve groepering van meerdere particuliere computernetwerken of hosts binnen dezelfde infrastructuur."""

        ipAdresField = DteIPv4Adres()
        ipAdresField.naam = "ipAdres"
        ipAdresField.label = "ip adres"
        ipAdresField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ipAdres"
        ipAdresField.definition = "Het IP-adres van de hardware."
        ipAdresField.constraints = ""
        ipAdresField.usagenote = ""
        ipAdresField.deprecated_version = ""
        self.ipAdres = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=ipAdresField)
        """Het IP-adres van de hardware."""

        self.licentie = StringField(naam="licentie",
                                    label="licentie",
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.licentie",
                                    definition="De licentie van het OS of de licentie van de hardware voor support/garantie op componenten.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De licentie van het OS of de licentie van de hardware voor support/garantie op componenten."""

        self.os = KeuzelijstField(naam="os",
                                  label="OS",
                                  lijst=KlHardwareOS(),
                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.os",
                                  definition="Het besturingssysteem dat op de hardware draait.",
                                  constraints="",
                                  usagenote="",
                                  deprecated_version="")
        """Het besturingssysteem dat op de hardware draait."""

        self.ram = KwantWrdInGigabyte()
        """De grootte van het werkgeheugen."""
        self.ram.naam = "ram"
        self.ram.label = "RAM"
        self.ram.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#HardwareToegang.ram"
        self.ram.definition = "De grootte van het werkgeheugen."
        self.ram.constraints = ""
        self.ram.usagenote = ""
        self.ram.deprecated_version = ""
