# coding=utf-8
from OTLMOW.OTLModel.Classes.Bebakening import Bebakening
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Reflectorpaal(Bebakening, PuntGeometrie):
    """Een kunststoffen paal met reflector om het verkeer te geleiden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Reflectorpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Bebakening.__init__(self)
        PuntGeometrie.__init__(self)
