# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stortdraad(AndereLaag, LijnGeometrie):
    """Staaldraad omwikkeld met een laag plastic ter bescherming tegen vocht, vooral gebruikt als stut voor stortsteen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortdraad'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        LijnGeometrie.__init__(self)
