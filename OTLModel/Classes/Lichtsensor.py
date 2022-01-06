from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtsensor(AIMNaamObject):
    """Sensor die de intensiteit van het invallende licht meet."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtsensor"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
