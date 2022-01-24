# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DNB import DNB


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBLaagspanning(DNB):
    """Aansluiting op het laagspanningsnet van de distributienetbeheerder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
