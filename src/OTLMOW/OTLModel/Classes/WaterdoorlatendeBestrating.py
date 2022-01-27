# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Bestrating import Bestrating
from src.OTLMOW.OTLModel.Datatypes.KlAardWBSS import KlAardWBSS
from src.OTLMOW.OTLModel.Datatypes.KlBestratingAfwerking import KlBestratingAfwerking
from src.OTLMOW.OTLModel.Datatypes.KlBestratingselementAfmetingLxB import KlBestratingselementAfmetingLxB
from src.OTLMOW.OTLModel.Datatypes.KlWBSSType import KlWBSSType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WaterdoorlatendeBestrating(Bestrating):
    """Betonstraatstenen of betontegels die omwille van hun vormkenmerken (bv. drainageopeningen of verbrede voegen) of betonstructuur (poreus beton met een open korrelopbouw) water doorlaten zoals omschreven in PTV 122."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aard = OTLAttribuut(field=KlAardWBSS,
                                  naam='aard',
                                  label='aard',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.aard',
                                  definition='Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is.')

        self._afmetingVanBestratingselementLxB = OTLAttribuut(field=KlBestratingselementAfmetingLxB,
                                                              naam='afmetingVanBestratingselementLxB',
                                                              label='afmeting van bestratingselement LxB',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afmetingVanBestratingselementLxB',
                                                              definition='De lengte en breedte van het bestratingselement in millimeter.')

        self._afwerking = OTLAttribuut(field=KlBestratingAfwerking,
                                       naam='afwerking',
                                       label='afwerking',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.afwerking',
                                       definition='Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels.')

        self._type = OTLAttribuut(field=KlWBSSType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WaterdoorlatendeBestrating.type',
                                  definition='Het type van waterdoorlatende betonstraatstenen of betontegels.')

    @property
    def aard(self):
        """Het kenmerk of de vorm van de waterdoorlatende betonstraatsteen waardoor infiltratie van hemelwater in de bodem mogelijk is."""
        return self._aard.waarde

    @aard.setter
    def aard(self, value):
        self._aard.set_waarde(value, owner=self)

    @property
    def afmetingVanBestratingselementLxB(self):
        """De lengte en breedte van het bestratingselement in millimeter."""
        return self._afmetingVanBestratingselementLxB.waarde

    @afmetingVanBestratingselementLxB.setter
    def afmetingVanBestratingselementLxB(self, value):
        self._afmetingVanBestratingselementLxB.set_waarde(value, owner=self)

    @property
    def afwerking(self):
        """Bepaling van de afwerking van de waterdoorlatende betonstraatstenen of betontegels."""
        return self._afwerking.waarde

    @afwerking.setter
    def afwerking(self, value):
        self._afwerking.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van waterdoorlatende betonstraatstenen of betontegels."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
