# coding=utf-8
from OTLMOW.OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Onderwatervegetatie(BegroeidVoorkomen, PuntGeometrie, VlakGeometrie):
    """Vegetatie die zich onder het wateroppervlak bevindt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Onderwatervegetatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BegroeidVoorkomen.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)
