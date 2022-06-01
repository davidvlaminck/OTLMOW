# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcExterneReferentie import DtcExterneReferentie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitsgroep(NaampadObject):
    """Groepering om de flitspalen van een kruispunt of bepaalde zone in onder te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

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

    @property
    def externeReferentie(self):
        """Referentie zoals gekend bij een externe partij bv. aannemer, VLCC, ..."""
        return self._externeReferentie.get_waarde()

    @externeReferentie.setter
    def externeReferentie(self, value):
        self._externeReferentie.set_waarde(value, owner=self)

    @property
    def isRoodLicht(self):
        """Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft."""
        return self._isRoodLicht.get_waarde()

    @isRoodLicht.setter
    def isRoodLicht(self, value):
        self._isRoodLicht.set_waarde(value, owner=self)
