# coding=utf-8
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IPBackbone(NaampadObject, GeenGeometrie):
    """Netwerk dat bestaat uit meerdere L3 switches. Zij verbinden de verschillende L2 access structuren met de datacentres"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#IPBackbone'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        GeenGeometrie.__init__(self)
