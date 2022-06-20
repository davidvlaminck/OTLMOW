# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.NaampadObject import NaampadObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Flitsgroep(NaampadObject, VlakGeometrie):
    """Groepering om de flitspalen van een kruispunt of bepaalde zone in onder te brengen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._isRoodLicht = OTLAttribuut(field=BooleanField,
                                         naam='isRoodLicht',
                                         label='is rood licht',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Flitsgroep.isRoodLicht',
                                         definition='Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft.',
                                         owner=self)

    @property
    def isRoodLicht(self):
        """Duidt aan of de groepering een snelheids- of roodlichtcamera installatie betreft."""
        return self._isRoodLicht.get_waarde()

    @isRoodLicht.setter
    def isRoodLicht(self, value):
        self._isRoodLicht.set_waarde(value, owner=self)
