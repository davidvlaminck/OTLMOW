# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Bestrating import Bestrating
from src.OTLMOW.OTLModel.Datatypes.DtcBSSRandafwerking import DtcBSSRandafwerking
from src.OTLMOW.OTLModel.Datatypes.KlBSSType import KlBSSType
from src.OTLMOW.OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from src.OTLMOW.OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanBetonstraatsteen(Bestrating):
    """Bestrating van geprefabriceerde stenen in beton die (in de afgesproken mate) voldoen aan de vereisten van NBN EN 1338 en NBN B21-311."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.')

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.afwerking',
                                       definition='Bepaling van afwerking van de betonstraatstenen.')

        self._randafwerking = OTLAttribuut(field=DtcBSSRandafwerking,
                                           naam='randafwerking',
                                           label='randafwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.randafwerking',
                                           definition='De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt.')

        self._type = OTLAttribuut(field=KlBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.type',
                                  definition='Het type betonstraatsteen.')

    @property
    def afmetingVanBestratingselementLxB(self):
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.waarde

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self):
        """Bepaling van afwerking van de betonstraatstenen."""
        return self._afwerking.waarde

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def randafwerking(self):
        """De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt."""
        return self._randafwerking.waarde

    @randafwerking.setter
    def randafwerking(self, value):
        self._randafwerking.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type betonstraatsteen."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
