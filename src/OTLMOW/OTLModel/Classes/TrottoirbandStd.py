# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLMOW.OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLMOW.OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLMOW.OTLModel.Datatypes.KlLETrottoirbandType import KlLETrottoirbandType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting,bestemd om de rand van de verharding te beschermen en te versterken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.norm',
                                  definition='De gestandaardiseerde trottoirband volgens aangeduide norm.')

        self._type = OTLAttribuut(field=KlLETrottoirbandType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.type',
                                  definition='Bepaling van het type van trottoirband.')

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandStd.vorm',
                                  definition='Bepaling van de vorm van de trottoirband.')

    @property
    def norm(self):
        """De gestandaardiseerde trottoirband volgens aangeduide norm."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Bepaling van het type van trottoirband."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """Bepaling van de vorm van de trottoirband."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
