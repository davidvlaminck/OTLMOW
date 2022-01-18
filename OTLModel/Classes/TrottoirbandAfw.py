# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AfwijkendeKantopsluiting import AfwijkendeKantopsluiting


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandAfw(AfwijkendeKantopsluiting, AttributeInfo):
    """Afwijkende kantopsluiting,bestemd om de rand van de verharding te beschermen en te versterken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandAfw'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfwijkendeKantopsluiting.__init__(self)
        AttributeInfo.__init__(self)
