# coding=utf-8
from OTLMOW.OTLModel.Classes.AndereLaag import AndereLaag
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeexpandeerdPolystyreen(AndereLaag, VlakGeometrie):
    """Geëxpandeerd polystyreen of PS-hardschuim is een karakteristieke en vrijwel altijd witte kunststof, in de volksmond piepschuim genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GeexpandeerdPolystyreen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)
