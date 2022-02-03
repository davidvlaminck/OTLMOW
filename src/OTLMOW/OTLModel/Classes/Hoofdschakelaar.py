# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoofdschakelaar(AIMNaamObject, PuntGeometrie):
    """Algemene automatische zekering waarmee de volledige installatie buiten spanning kan worden gesteld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)
