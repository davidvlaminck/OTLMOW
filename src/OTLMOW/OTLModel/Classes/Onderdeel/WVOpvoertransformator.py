# coding=utf-8
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVOpvoertransformator(AIMObject, PuntGeometrie):
    """Toestel voor het opvoeren van de spanning, bij wegverlichtingsinstallaties gebruikt om de spanning te verhogen indien deze te laag geworden is wegens de kabelverliezen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)
