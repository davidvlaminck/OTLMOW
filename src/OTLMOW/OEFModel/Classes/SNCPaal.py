# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SNCPaal(EMObject):
    """VHS flitspalen : paal van een Snelheidscamera-installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SNCPaal'
    label = 'Snelheidscamerapaal'

    def __init__(self):
        super().__init__()

        self._interneRoestvorming = EMAttribuut(field=StringField,
                                                naam='interne roestvorming',
                                                label='interne roestvorming',
                                                objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.interneRoestvorming',
                                                definitie='keuzelijst en schaalverdeling volgens inspectiehandboek')

    @property
    def interneRoestvorming(self):
        """keuzelijst en schaalverdeling volgens inspectiehandboek"""
        return self._interneRoestvorming.waarde

    @interneRoestvorming.setter
    def interneRoestvorming(self, value):
        self._interneRoestvorming.set_waarde(value, owner=self)

