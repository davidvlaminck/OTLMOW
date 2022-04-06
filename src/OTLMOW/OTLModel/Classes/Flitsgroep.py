# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie
from OTLMOW.OTLModel.Datatypes.KlTypeFlitspaal import KlTypeFlitspaal
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitsgroep(NaampadObject, VlakGeometrie):
    """Groepering om de flitspalen van een kruispunt of bepaalde zone in onder te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._externeReferentie = OTLAttribuut(field=DtcExterneReferentie,
                                               naam='externeReferentie',
                                               label='externe referentie',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep.externeReferentie',
                                               definition='Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ...',
                                               owner=self)

        self._isRoodLicht = OTLAttribuut(field=BooleanField,
                                         naam='isRoodLicht',
                                         label='is rood licht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep.isRoodLicht',
                                         definition='Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlTypeFlitspaal,
                                  naam='type',
                                  label='type SNC/RLC',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep.type',
                                  definition='Het type van de flitspalen in de zone.',
                                  owner=self)

    @property
    def externeReferentie(self):
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.waarde

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)

    @property
    def isRoodLicht(self):
        """Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft."""
        return self._isRoodLicht.waarde

    @isRoodLicht.setter
    def isRoodLicht(self, value):
        self._isRoodLicht.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de flitspalen in de zone."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
