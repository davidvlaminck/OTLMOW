# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lensplaat(AIMObject, PuntGeometrie):
    """Afsluitplaat van de camerakast."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lensplaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
