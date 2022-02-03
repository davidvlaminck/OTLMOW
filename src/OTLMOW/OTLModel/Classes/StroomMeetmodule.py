# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class StroomMeetmodule(AIMNaamObject, PuntGeometrie):
    """Differentieel dat de spanning op de leidingen detecteert en fouten doorgeeft naar de PLC."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#StroomMeetmodule'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)
