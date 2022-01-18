# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLModel.Datatypes.KlLEKantstrookType import KlLEKantstrookType
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class KantstrookStd(GestandaardiseerdeKantopsluiting, AttributeInfo):
    """Gestandaardiseerde kantopsluiting, bestemd om de verharding steun te geven."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        GestandaardiseerdeKantopsluiting.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.breedte',
                                     definition='De breedte van de gestandaardiseerde kantstrook in centimeter.')

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.dikte',
                                   definition='De dikte van de gestandaardiseerde kantstrook in centimeter.')

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.norm',
                                  definition='De gestandaardiseerd kantstrook volgens aangeduide norm.')

        self._type = OTLAttribuut(field=KlLEKantstrookType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KantstrookStd.type',
                                  definition='Het type van gestandaardiseerde kantstrook.')

    @property
    def breedte(self):
        """De breedte van de gestandaardiseerde kantstrook in centimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self):
        """De dikte van de gestandaardiseerde kantstrook in centimeter."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def norm(self):
        """De gestandaardiseerd kantstrook volgens aangeduide norm."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van gestandaardiseerde kantstrook."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
