# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynamischeVluchtwegindicatie(AIMObject, AttributeInfo):
    """Armaturen die ingezet worden indien er alternatieve vluchtconcepten worden toegepast. De vluchtroute loopt dan meestal gedeeltelijk door de ondersteunende koker. De borden geven de te volgen vluchtroute aan en zijn pas zichtbaar zodra ze worden ingeschakeld. Bij evacuatie kan er ook een extra ondersteunende omroepbericht worden ingezet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynamischeVluchtwegindicatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
