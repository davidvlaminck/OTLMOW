# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlHoogtedetectieMerk import KlHoogtedetectieMerk
from src.OTLMOW.OTLModel.Datatypes.KlHoogtedetectieModelnaam import KlHoogtedetectieModelnaam
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoogtedetectie(AIMNaamObject):
    """Hoogtedetectiesysteem voor het voorkomen van schade aan kunstwerken. Stuurt vaak een dynamisch bord aan. Voor handhaving staat het in relatie met een ANPR-camera."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._detectiehoogte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='detectiehoogte',
                                            label='detectiehoogte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.detectiehoogte',
                                            definition='De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen.')

        self._merk = OTLAttribuut(field=KlHoogtedetectieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.merk',
                                  usagenote='volgens een keuzelijst',
                                  definition='Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent.')

        self._modelnaam = OTLAttribuut(field=KlHoogtedetectieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.modelnaam',
                                       usagenote='Uit een keuzelijst.',
                                       definition='De modelnaam van de hoogtedetectie.')

    @property
    def detectiehoogte(self):
        """De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen."""
        return self._detectiehoogte.waarde

    @detectiehoogte.setter
    def detectiehoogte(self, value):
        self._detectiehoogte.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de hoogtedetectie."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
