# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.BloemrijkGraslandGraslandfase4 import BloemrijkGraslandGraslandfase4


# Generated with OTLClassCreator. To modify: extend, do not edit
class BloemrijkStruisgrasgrasland(BloemrijkGraslandGraslandfase4):
    """G4d - akkerhoornbloem, gewone veldbies, gewoon
biggenkruid, gewoon duizendblad, gewoon
struisgras, hazenpootje, klein vogelpootje,
kleine klaver, kleine leeuwentand,
knolboterbloem, muizenoor, schapenzuring,
smalle weegbree, vroege haver, zilverhaver."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BloemrijkStruisgrasgrasland'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
