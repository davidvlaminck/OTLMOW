# coding=utf-8
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aftakking(AIMNaamObject, PuntGeometrie):
    """Groep van stroomkringen specifiek bedoeld voor de aansturing van wegverlichting.In het typeschema autosnelwegen worden er standaard 4 aftakkingen voorzien: middenberm (hoofdrijbaan),op- en afritten + signalisatie,gewestweg,parking."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)
