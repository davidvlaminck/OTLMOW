# coding=utf-8
from OTLMOW.OTLModel.Classes.Geleiding import Geleiding
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stobbenwal(Geleiding, LijnGeometrie):
    """Wortelkluiten of ander houtmateriaal (zoals stamhout) om beschutting en geleiding van kleinere diersoorten zoals muizen, egels."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stobbenwal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Geleiding.__init__(self)
        LijnGeometrie.__init__(self)
