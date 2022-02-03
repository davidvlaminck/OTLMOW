# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class RLCPaal(EMObject):
    """VHS flitspalen : paal van een Roodlichtcamera-installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RLCPaal'
    label = 'Roodlichtcamerapaal'

    def __init__(self):
        super().__init__()

        self._interneRoestvorming = EMAttribuut(field=StringField,
                                                naam='interne roestvorming',
                                                label='interne roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.interneRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek',
                                                owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

    @property
    def interneRoestvorming(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._interneRoestvorming.waarde

    @interneRoestvorming.setter
    def interneRoestvorming(self, value):
        self._interneRoestvorming.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

