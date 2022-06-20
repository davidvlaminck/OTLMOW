# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Contourverlichting(AIMObject, PuntGeometrie):
    """Groene ledstrip verlichting die de vluchtdeur omrand en zo de visibiliteit van de vluchtdeur en de vluchtweg vergroot."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contourverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
