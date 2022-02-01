# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class LS(EMObject):
    """Laagspanningsaansluiting. Deze zit meestal in een Kast of Cabine (behuizing) en voedt meestal een LSDeel."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#LS'
    label = 'Laagspanningsaansluiting'

    def __init__(self):
        super().__init__()

        self._installatieverantwConformArt266Arei = EMAttribuut(field=StringField,
                                                                naam='installatieverantw conform art 266 AREI',
                                                                label='installatieverantw conform art 266 AREI',
                                                                objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.installatieverantwConformArt266Arei',
                                                                definitie='Definitie nog toe te voegen voor eigenschap installatieverantw conform art 266 AREI')

    @property
    def installatieverantwConformArt266Arei(self):
        """Definitie nog toe te voegen voor eigenschap installatieverantw conform art 266 AREI"""
        return self._installatieverantwConformArt266Arei.waarde

    @installatieverantwConformArt266Arei.setter
    def installatieverantwConformArt266Arei(self, value):
        self._installatieverantwConformArt266Arei.set_waarde(value, owner=self)

