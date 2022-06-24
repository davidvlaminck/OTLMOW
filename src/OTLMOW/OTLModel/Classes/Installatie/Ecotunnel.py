# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecotunnel(AIMObject, VlakGeometrie):
    """Een (grote) ecotunnel is een tunnel onder een grote weg, waarlangs dieren veilig de overkant kunnen bereiken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecotunnel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)
