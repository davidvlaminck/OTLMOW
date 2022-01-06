from OTLModel.Classes.PTModuleMetFirmware import PTModuleMetFirmware
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPtKARModemProtocol import KlPtKARModemProtocol


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTKARModem(PTModuleMetFirmware):
    """Modem die KAR signalen, korte afstands radiosignalen, kan ontvangen van de KAR-module die geïnstalleerd is op het openbaar vervoer voertuig. Het voertuig meldt zich zo via virtuele lussen, gedefinieerd op basis van GPS- positie, aan bij de PT regelaar."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.protocolOVVoertuig = KeuzelijstField(naam="protocolOVVoertuig",
                                                  label="protocol OV-voertuig",
                                                  lijst=KlPtKARModemProtocol(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem.protocolOVVoertuig",
                                                  definition="Beschrijft het protocol dat gebruikt wordt om te communiceren met een OV-voertuig.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Beschrijft het protocol dat gebruikt wordt om te communiceren met een OV-voertuig."""

        self.protocolRegelaar = KeuzelijstField(naam="protocolRegelaar",
                                                label="protocol regelaar",
                                                lijst=KlPtKARModemProtocol(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTKARModem.protocolRegelaar",
                                                definition="Beschrijft het protocol dat gebruikt wordt om te communiceren met een regelaar.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Beschrijft het protocol dat gebruikt wordt om te communiceren met een regelaar."""
