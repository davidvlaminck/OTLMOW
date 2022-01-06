from OTLModel.Classes.PTModuleMetFirmware import PTModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTModem(PTModuleMetFirmware):
    """Communicatiemodem van het personentransportbeïnvloedingssysteem die via het netwerk (3G-4G) communiceert."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTModem"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
