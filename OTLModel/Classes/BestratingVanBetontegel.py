# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.KlBSSType import KlBSSType
from OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanBetontegel(Bestrating):
    """Bestrating van geprefabriceerde platte stenen in beton die (in de afgesproken mate) voldoen aan de vereisten van NBN EN 1339 en NBN B21-211."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.')

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.afwerking',
                                       definition='Bepaling van afwerking van de betontegels.')

        self._type = OTLAttribuut(field=KlBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetontegel.type',
                                  definition='Het type betontegel.')

    @property
    def afmetingVanBestratingselementLxB(self):
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.waarde

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self):
        """Bepaling van afwerking van de betontegels."""
        return self._afwerking.waarde

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type betontegel."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
