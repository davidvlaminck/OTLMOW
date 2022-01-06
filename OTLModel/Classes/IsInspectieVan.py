# coding=utf-8
from OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsInspectieVan(DirectioneleRelatie):
    """De relatie geeft aan dat er een inspectie, proef of meting gedaan kan worden op een onderdeel of installatie. De bron van de relatie is de inspectie, het doel het onderdeel of de installatie waarbij de inspectie hoort."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsInspectieVan"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
