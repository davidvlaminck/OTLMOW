# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class RSSGroep(EMObject):
    """RSS groep : groep van RSS variabele rijstrooksignalisatieborden"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#RSSGroep'
    label = 'RSS groep'

    def __init__(self):
        super().__init__()

        self._type7 = EMAttribuut(field=StringField,
                                  naam='type',
                                  label='type',
                                  objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.type7',
                                  definitie='Definitie nog toe te voegen voor eigenschap type')

    @property
    def type7(self):
        """Definitie nog toe te voegen voor eigenschap type"""
        return self._type7.waarde

    @type7.setter
    def type7(self, value):
        self._type7.set_waarde(value, owner=self)

