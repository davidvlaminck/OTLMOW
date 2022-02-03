# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Handwiel(AIMObject, PuntGeometrie):
    """Een handwiel kan worden gebruikt voor het openen of sluiten van een afsluiter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Handwiel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
