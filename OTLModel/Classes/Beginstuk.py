from abc import abstractmethod
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Beginstuk(AfschermendeConstructie):
    """Abstracte voor een stuk aan het uiteinde van een geleideconstructie,met als doel een frontale botsing te reduceren gericht naar het naderende verkeer."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Beginstuk"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
