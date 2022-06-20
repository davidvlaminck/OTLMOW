# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Bestrating import Bestrating
from OTLMOW.OTLModel.Datatypes.DtcBSSRandafwerking import DtcBSSRandafwerking
from OTLMOW.OTLModel.Datatypes.KlBSSType import KlBSSType
from OTLMOW.OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from OTLMOW.OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB


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
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.',
                                                              owner=self)

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.afwerking',
                                       definition='Bepaling van afwerking van de betonstraatstenen.',
                                       owner=self)

        self._randafwerking = OTLAttribuut(field=DtcBSSRandafwerking,
                                           naam='randafwerking',
                                           label='randafwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.randafwerking',
                                           definition='De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt.',
                                           owner=self)

        self._type = OTLAttribuut(field=KlBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanBetonstraatsteen.type',
                                  definition='Het type betonstraatsteen.',
                                  owner=self)

    @property
    def afmetingVanBestratingselementLxB(self):
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.get_waarde()

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self):
        """Bepaling van afwerking van de betonstraatstenen."""
        return self._afwerking.get_waarde()

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def randafwerking(self):
        """De wijze waarop de rand van de betonstraatsteenverharding is afgewerkt."""
        return self._randafwerking.get_waarde()

    @randafwerking.setter
    def randafwerking(self, value):
        self._randafwerking.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type betonstraatsteen."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
