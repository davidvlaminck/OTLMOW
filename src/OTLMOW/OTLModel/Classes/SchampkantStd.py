# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.GestandaardiseerdeKantopsluiting import GestandaardiseerdeKantopsluiting
from OTLMOW.OTLModel.Datatypes.DtcLENorm import DtcLENorm
from OTLMOW.OTLModel.Datatypes.KlLESchampkantType import KlLESchampkantType
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchampkantStd(GestandaardiseerdeKantopsluiting):
    """Gestandaardiseerde kantopsluiting, die zones van voertuigenverkeer onderling of voertuigenzones van andere verkeerszones scheidt en de overschrijding door voertuigen bemoeilijkt maar geen voertuigkerende functie heeft."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.breedte',
                                     definition='De breedte van de gestandaardiseerde schampkant in centimeter.')

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.dikte',
                                   definition='De dikte van de gestandaardiseerde schampkant in centimeter.')

        self._norm = OTLAttribuut(field=DtcLENorm,
                                  naam='norm',
                                  label='norm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.norm',
                                  definition='De gestandaardiseerde schampkant volgens aangeduide norm.')

        self._type = OTLAttribuut(field=KlLESchampkantType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SchampkantStd.type',
                                  definition='Het type van gestandaardiseerde schampkant.')

    @property
    def breedte(self):
        """De breedte van de gestandaardiseerde schampkant in centimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self):
        """De dikte van de gestandaardiseerde schampkant in centimeter."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def norm(self):
        """De gestandaardiseerde schampkant volgens aangeduide norm."""
        return self._norm.waarde

    @norm.setter
    def norm(self, value):
        self._norm.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van gestandaardiseerde schampkant."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
