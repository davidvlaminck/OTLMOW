# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlHoogtedetectieMerk import KlHoogtedetectieMerk
from OTLMOW.OTLModel.Datatypes.KlHoogtedetectieModelnaam import KlHoogtedetectieModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hoogtedetectie(AIMNaamObject, PuntGeometrie):
    """Hoogtedetectiesysteem voor het voorkomen van schade aan kunstwerken. Stuurt vaak een dynamisch bord aan. Voor handhaving staat het in relatie met een ANPR-camera."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._detectiehoogte = OTLAttribuut(field=KwantWrdInMeter,
                                            naam='detectiehoogte',
                                            label='detectiehoogte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.detectiehoogte',
                                            definition='De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen.',
                                            owner=self)

        self._merk = OTLAttribuut(field=KlHoogtedetectieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.merk',
                                  usagenote='volgens een keuzelijst',
                                  definition='Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHoogtedetectieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoogtedetectie.modelnaam',
                                       usagenote='Uit een keuzelijst.',
                                       definition='De modelnaam van de hoogtedetectie.',
                                       owner=self)

    @property
    def detectiehoogte(self):
        """De ingestelde hoogtelimiet waarboven het systeem voor hoogtedetectie een detectiesignaal moet uitsturen."""
        return self._detectiehoogte.get_waarde()

    @detectiehoogte.setter
    def detectiehoogte(self, value):
        self._detectiehoogte.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van het systeem voor hoogtedetectie.Verwijst naar de fabrikant of producent."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de hoogtedetectie."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
