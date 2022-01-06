from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVrComKaartTypeOpslaggeheugen import KlVrComKaartTypeOpslaggeheugen
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRCommunicatiekaart(VRModuleMetFirmware):
    """Modem die alle toestandswijzigingen van de stuurkaart doorgeeft aan het afstandsbewakingssysteem. De module maakt continue een backup van alle log en data gegevens en slaat deze op op de aanwezige SD kaart. Tevens wordt de module ook gebruikt om vanop afstand te kunnen communiceren met de regelaar"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.dnsNaam = StringField(naam="dnsNaam",
                                   label="DNS naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.dnsNaam",
                                   definition="De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """De DNSNaam (ook \"volledige domein naam\" genoemd ) is een unieke naam binnen het Domain Name System (DNS), het naamgevingssysteem waarmee computers, webservers, diensten en  toepassing op een unieke manier kunnen worden geïdentificeerd. Deze bevat zowel de hostname en de top level domein naam bv. 120c8-ar1.belfa.be."""

        self.heeftSmartguard = BooleanField(naam="heeftSmartguard",
                                            label="heeft smartguard",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.heeftSmartguard",
                                            definition="Smartguard aanwezig?",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Smartguard aanwezig?"""

        self.ipAdres = DteIPv4Adres()
        """IP-adres."""
        self.ipAdres.naam = "ipAdres"
        self.ipAdres.label = "ipv4 adres"
        self.ipAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.ipAdres"
        self.ipAdres.definition = "IP-adres."
        self.ipAdres.constraints = ""
        self.ipAdres.usagenote = ""
        self.ipAdres.deprecated_version = ""

        self.telefoonnummer = StringField(naam="telefoonnummer",
                                          label="telefoonnummer",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.telefoonnummer",
                                          definition="Telefoonnummer.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Telefoonnummer."""

        self.typeGeheugen = KeuzelijstField(naam="typeGeheugen",
                                            label="type geheugen",
                                            lijst=KlVrComKaartTypeOpslaggeheugen(),
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.typeGeheugen",
                                            definition="Type opslaggeheugen op de aanwezige SD-kaart.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Type opslaggeheugen op de aanwezige SD-kaart."""

        self.uitvoering = StringField(naam="uitvoering",
                                      label="uitvoering",
                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRCommunicatiekaart.uitvoering",
                                      definition="Type van communicatiekaart.",
                                      constraints="",
                                      usagenote="",
                                      deprecated_version="")
        """Type van communicatiekaart."""
