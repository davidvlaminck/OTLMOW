from OTLModel.Classes.NaampadObject import NaampadObject


# Generated with OTLClassCreator
class Hulppost(NaampadObject):
    """De verzameling van hulpgerelateerde technieken en objecten op een bepaalde plaats, bv.een nis in een tunnel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
