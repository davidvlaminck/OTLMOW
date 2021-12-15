from OTLModel.Verification.AIMNaamObject import AIMNaamObject


class Hoofdschakelaar(AIMNaamObject):
    """Algemene automatische zekering waarmee de volledige installatie buiten spanning kan worden gesteld."""
    def __init__(self):
        pass

    typeUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""
