# coding=utf-8
from OTLMOW.OTLModel.Classes.PutRelatie import PutRelatie
from OTLMOW.OTLModel.Classes.Put import Put
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Infiltratievoorziening(PutRelatie, Put, VlakGeometrie):
    """Voorziening voor infiltratie van onvervuild water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Infiltratievoorziening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)
        VlakGeometrie.__init__(self)
