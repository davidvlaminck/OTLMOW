# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class Flitscamera(AIMObject, PuntGeometrie):
    """Cameratoestel waarmee de overtredingen vastgelegd worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=StringField,  # TODO KlFlitscameraMerk
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera.merk',
                                  definition='Het merk van de flitscamera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,  # TODO KlFlitscameraModelnaam
                                  naam='modelnaam',
                                  label='modelnaam',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera.modelnaam',
                                  definition='Het model of productrange van de flitspaalbehuizing.',
                                  owner=self)

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                  naam='externeReferentie',
                                  label='externe referentie',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Flitscamera.externeReferentie',
                                  definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...',
                                  owner=self)

    @property
    def merk(self):
        """Het merk van de flitscamera."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Het model of productrange van een flitscamera."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def externeReferentie(self):
        """Het model of productrange van een flitscamera."""
        return self._externeReferentie.waarde

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)

