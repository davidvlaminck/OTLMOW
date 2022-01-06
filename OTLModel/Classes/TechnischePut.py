# coding=utf-8
from OTLModel.Classes.Behuizing import Behuizing


# Generated with OTLClassCreator. To modify: extend, do not edit
class TechnischePut(Behuizing):
    """Ondergrondse toezichtsput (manhole). Deze kan telecom installaties (glasvezel,koper) of elektriciteitskabels bevatten. 
Kan uit verschillende materialen bestaan: polycarbonaat,beton,gemetst,of staal."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TechnischePut"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
