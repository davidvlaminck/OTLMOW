# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleidingsverlichting(AIMObject, PuntGeometrie, LijnGeometrie):
    """Verlichting die de gestrande weggebruiker begeleiding biedt op handhoogte langs de vluchtroute tot aan een vluchtdeur of tot aan een veilige locatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleidingsverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
