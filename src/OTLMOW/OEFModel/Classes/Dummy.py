# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Dummy(EMObject):
    """DUMMY Installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Dummy'
    label = 'Dummy'

    def __init__(self):
        super().__init__()

        self._notitieDummy = EMAttribuut(field=StringField,
                                         naam='notitie (DUMMY)',
                                         label='notitie (DUMMY)',
                                         objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#Dummy.notitieDummy',
                                         definitie='Definitie nog toe te voegen voor eigenschap notitie (DUMMY)',
                                         owner=self)

    @property
    def notitieDummy(self):
        """Definitie nog toe te voegen voor eigenschap notitie (DUMMY)"""
        return self._notitieDummy.waarde

    @notitieDummy.setter
    def notitieDummy(self, value):
        self._notitieDummy.set_waarde(value, owner=self)

