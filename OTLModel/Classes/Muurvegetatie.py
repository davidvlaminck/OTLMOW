from OTLModel.Classes.VegetatieElement import VegetatieElement


# Generated with OTLClassCreator
class Muurvegetatie(VegetatieElement):
    """Muurvegetaties zijn gebonden aan door de mens gecreëerde stenige, doorgaans steile tot verticale standplaatsen. Voorbeelden zijn kerkhofmuren, stadswallen, ruïnes, kademuren, oude forten en bunkers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Muurvegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
