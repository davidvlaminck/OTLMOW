# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Datatypes.KlBatterijMerk import KlBatterijMerk
from OTLMOW.OTLModel.Datatypes.KlBatterijModelnaam import KlBatterijModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Batterij(Voedingspunt, PuntGeometrie):
    """Element bestaande uit meerdere elektrochemische cellen voor het leveren van elektriciteit,die ontstaat door de omzetting van opgeslagen chemische energie in elektrische energie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Voedingspunt.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlBatterijMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.merk',
                                  definition='Merk van de batterij.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlBatterijModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Batterij.modelnaam',
                                       definition='Modelnaam van de batterij.',
                                       owner=self)

    @property
    def merk(self):
        """Merk van de batterij."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de batterij."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
