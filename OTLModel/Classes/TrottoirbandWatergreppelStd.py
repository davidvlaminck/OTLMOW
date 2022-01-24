# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.DtcTrottoirbandVorm import DtcTrottoirbandVorm
from OTLModel.Datatypes.KlLETrottoirbandWatergreppelType import KlLETrottoirbandWatergreppelType


# Generated with OTLClassCreator. To modify: extend, do not edit
class TrottoirbandWatergreppelStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die een trottoirband en een watergreppel combineert in een geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.norm',
                                  definition='De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm.')

        self._type = OTLAttribuut(field=KlLETrottoirbandWatergreppelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.type',
                                  definition='Het type van gestandaardiseerde trottoirband_watergreppel.')

        self._vorm = OTLAttribuut(field=DtcTrottoirbandVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#TrottoirbandWatergreppelStd.vorm',
                                  definition='De vorm van de gestandaardiseerde trottoirband_watergreppel.')

    @property
    def norm(self):
        """De gestandaardiseerde trottoirband_watergreppel volgens aangeduide norm."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van gestandaardiseerde trottoirband_watergreppel."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de gestandaardiseerde trottoirband_watergreppel."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
