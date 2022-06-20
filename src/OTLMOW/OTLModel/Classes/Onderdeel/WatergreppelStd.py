# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLMOW.OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLMOW.OTLModel.Datatypes.KlLEWatergreppelType import KlLEWatergreppelType


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
                                        definition='Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit.',
                                        owner=self)

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.norm',
                                  definition='De gestandaardiseerde watergreppel volgens aangeduide norm.',
                                  owner=self)

        self._type = OTLAttribuut(field=KlLEWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde watergreppel.',
                                  owner=self)

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WatergreppelStd.vorm',
                                  definition='De vorm van de watergreppel.',
                                  owner=self)

    @property
    def isVerholen(self):
        """Aanduiding of de watergreppel verholen is. Verholen goten hebben een kleine sleufopening en een grote afvoercapaciteit."""
        return self._isVerholen.get_waarde()

    @isVerholen.setter
    def isVerholen(self, value):
        self._isVerholen.set_waarde(value, owner=self)

    @property
    def norm(self):
        """De gestandaardiseerde watergreppel volgens aangeduide norm."""
        return self._norm.get_waarde()

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van gestandaardiseerde watergreppel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de watergreppel."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
