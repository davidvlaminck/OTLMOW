# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoofdschakelaar(AIMNaamObject):
    """Algemene automatische zekering waarmee de volledige installatie buiten spanning kan worden gesteld."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
