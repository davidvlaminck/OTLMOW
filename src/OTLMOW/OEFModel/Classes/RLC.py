# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class RLC(EMObject):
    """VHS flitspalen : Installatie Roodlichtcamera - Dit type flitspaal registreert zowel roodlichtnegaties als snelheidsovertredingen. Zij worden opgesteld op kruispunten met verkeerslichten."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RLC'
    label = 'Roodlichtcamera installatie'

    def __init__(self):
        super().__init__()

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie')

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

