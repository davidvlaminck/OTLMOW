from OTLModel.Classes.PTModuleMetFirmware import PTModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRadio(PTModuleMetFirmware):
    """Module voor het verzenden en ontvangen van berichten komende van een radio uit een andere verkeersregelaar of een kast op afstand."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRadio"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
