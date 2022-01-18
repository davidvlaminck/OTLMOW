# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Grasland import Grasland


# Generated with OTLClassCreator. To modify: extend, do not edit
class GrassenmixGraslandfase1(Grasland, AttributeInfo):
    """G1 - Groen lappendeken met soorten uit G0 + kruipende boterbloem, paardenbloem,gewone hoornbloem (in enkelemonospecifieke haarden)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GrassenmixGraslandfase1'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Grasland.__init__(self)
