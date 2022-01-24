# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecotunnel(AIMObject):
    """Een (grote) ecotunnel is een tunnel onder een grote weg, waarlangs dieren veilig de overkant kunnen bereiken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecotunnel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
