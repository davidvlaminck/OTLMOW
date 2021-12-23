from OTLModel.Classes.NaampadObject import NaampadObject


# Generated with OTLClassCreator
class IPBackbone(NaampadObject):
    """Netwerk dat bestaat uit meerdere L3 switches. Zij verbinden de verschillende L2 access structuren met de datacentres"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#IPBackbone"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
