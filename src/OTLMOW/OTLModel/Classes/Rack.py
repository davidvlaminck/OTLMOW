# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from src.OTLMOW.OTLModel.Datatypes.KlRackMerk import KlRackMerk
from src.OTLMOW.OTLModel.Datatypes.KlRackModelnaam import KlRackModelnaam
from src.OTLMOW.OTLModel.Datatypes.KlRackType import KlRackType
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rack(AIMNaamObject):
    """Interne draagstructuur binnen een behuizing voor (elektromechanische) toestellen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._diepte = OTLAttribuut(field=KwantWrdInCentimeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.diepte',
                                    definition='De diepte van het rack tussen de voorste en achterste rails.')

        self._hoogteInRU = OTLAttribuut(field=IntegerField,
                                        naam='hoogteInRU',
                                        label='hoogte in RU',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.hoogteInRU',
                                        definition='Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units).')

        self._huidigBeeld = OTLAttribuut(field=DtcDocument,
                                         naam='huidigBeeld',
                                         label='huidig beeld',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.huidigBeeld',
                                         definition='Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack.')

        self._merk = OTLAttribuut(field=KlRackMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.merk',
                                  definition='Merk waarmee de fabrikant dit type rack identificeert.')

        self._modelnaam = OTLAttribuut(field=KlRackModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.modelnaam',
                                       definition='Modelnaam waarmee de fabrikant dit type toestel identificeert.')

        self._rackType = OTLAttribuut(field=KlRackType,
                                      naam='rackType',
                                      label='Rack type',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rack.rackType',
                                      definition='Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types.')

    @property
    def diepte(self):
        """De diepte van het rack tussen de voorste en achterste rails."""
        return self._diepte.waarde

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def hoogteInRU(self):
        """Bruikbare ruimte om toestellen te monteren, uitgedrukt in RU (rack units)."""
        return self._hoogteInRU.waarde

    @hoogteInRU.setter
    def hoogteInRU(self, value):
        self._hoogteInRU.set_waarde(value, owner=self)

    @property
    def huidigBeeld(self):
        """Foto of schematische voorstelling van de huidige samenstelling van de samenstelling in het rack."""
        return self._huidigBeeld.waarde

    @huidigBeeld.setter
    def huidigBeeld(self, value):
        self._huidigBeeld.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk waarmee de fabrikant dit type rack identificeert."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam waarmee de fabrikant dit type toestel identificeert."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def rackType(self):
        """Geeft het type aan voor een rack volgens een keuzelijst van beschikbare types."""
        return self._rackType.waarde

    @rackType.setter
    def rackType(self, value):
        self._rackType.set_waarde(value, owner=self)
