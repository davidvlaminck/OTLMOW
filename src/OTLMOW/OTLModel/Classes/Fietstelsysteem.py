# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlFietstelsysteemMerk import KlFietstelsysteemMerk
from OTLMOW.OTLModel.Datatypes.KlFietstelsysteemModelnaam import KlFietstelsysteemModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Fietstelsysteem(AIMNaamObject, PuntGeometrie):
    """Toestel bij de fietstelinstallatie dat gegevens van detectielussen over passerende fietsers verzamelt en verwerkt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._afmetingen = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                        naam='afmetingen',
                                        label='afmetingen',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.afmetingen',
                                        definition='De afmetingen van het fietstelsysteem.',
                                        owner=self)

        self._merk = OTLAttribuut(field=KlFietstelsysteemMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.merk',
                                  definition='Merknaam van het fietstelsysteem.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlFietstelsysteemModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.modelnaam',
                                       definition='Naam van het model van het fietstelsysteem volgens de fabrikant.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Fietstelsysteem.technischeFiche',
                                             definition='Document met de technische specificaties van het fietstelsysteem.',
                                             owner=self)

    @property
    def afmetingen(self):
        """De afmetingen van het fietstelsysteem."""
        return self._afmetingen.waarde

    @afmetingen.setter
    def afmetingen(self, value):
        self._afmetingen.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van het fietstelsysteem."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Naam van het model van het fietstelsysteem volgens de fabrikant."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Document met de technische specificaties van het fietstelsysteem."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
