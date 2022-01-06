from OTLModel.Classes.VRModuleMetFirmware import VRModuleMetFirmware


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRBeveiligingskaart(VRModuleMetFirmware):
    """Processorkaart die de beveiligings- en bewakingsfunctie op zich neemt. Indien bij controle van de signalen een gevaarlijke status vastgesteld wordt, zorgt deze voor een omschakeling van het signaalsysteem naar een veilige status, nl. gecontroleerde uitschakeling"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRBeveiligingskaart"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
