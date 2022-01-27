# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DtcLENorm import DtcLENorm
from src.OTLMOW.OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from src.OTLMOW.OTLModel.Datatypes.KlLEWatergreppelType import KlLEWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, bestemd om water van de verharding op te vangen en af te voeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isVerholen = OTLAttribuut(field=BooleanField,
                                        naam='isVerholen',
                                        label='is verholen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.isVerholen',
                                        definition='Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit.')

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.norm',
                                  definition='De gestandaardiseerde watergreppel volgens aangeduide norm.')

        self._type = OTLAttribuut(field=KlLEWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde watergreppel.')

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.vorm',
                                  definition='De vorm van de watergreppel.')

    @property
    def isVerholen(self):
        """Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit."""
        return self._isVerholen.waarde

    @isVerholen.setter
    def isVerholen(self, value):
        self._isVerholen.set_waarde(value, owner=self)

    @property
    def norm(self):
        """De gestandaardiseerde watergreppel volgens aangeduide norm."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van gestandaardiseerde watergreppel."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de watergreppel."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
