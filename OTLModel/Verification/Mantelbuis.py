from OTLModel.Verification.Buis import Buis
from OTLModel.Verification.ContainerBuis import ContainerBuis


class Mantelbuis(Buis, ContainerBuis):
    """Een ondergrondse buis bestemd voor de doorvoer van kabels en/of leidingen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Mantelbuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Buis.__init__(self)
        ContainerBuis.__init__(self)
        # super(Buis, self).__init__()
        # super(ContainerBuis, self).__init__(self)

