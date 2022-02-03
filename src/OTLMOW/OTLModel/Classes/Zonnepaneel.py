# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLMOW.OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLMOW.OTLModel.Datatypes.KlZonnepaneelMerk import KlZonnepaneelMerk
from OTLMOW.OTLModel.Datatypes.KlZonnepaneelModelnaam import KlZonnepaneelModelnaam
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zonnepaneel(Voedingspunt, BevestigingGC, PuntGeometrie):
    """Toestel om elektrische energie op te wekken uit zonlicht met als doel het voeden van een installatie. Ook wel fotovoltaïsche cellen of zonnecellen genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BevestigingGC.__init__(self)
        Voedingspunt.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlZonnepaneelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.merk',
                                  definition='Het merk van het zonnepaneel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlZonnepaneelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.modelnaam',
                                       definition='De modelnaam van het zonnepaneel.',
                                       owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInWatt,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.vermogen',
                                      definition='Het vermogen van het zonnepaneel.',
                                      owner=self)

    @property
    def merk(self):
        """Het merk van het zonnepaneel."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van het zonnepaneel."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Het vermogen van het zonnepaneel."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
