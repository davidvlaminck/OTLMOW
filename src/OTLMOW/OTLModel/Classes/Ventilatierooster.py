# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ventilatierooster(AIMObject, PuntGeometrie):
    """Stuurt de luchtstromen van of naar een ventilator in de gewenste richting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ventilatierooster'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
