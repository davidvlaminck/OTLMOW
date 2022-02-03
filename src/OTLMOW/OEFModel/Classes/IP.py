# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class IP(EMObject):
    """IP-netwerkapparatuur"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#IP'
    label = 'IP-netwerkapparatuur'

    def __init__(self):
        super().__init__()

        self._ipAdres = EMAttribuut(field=StringField,
                                    naam='IP-adres',
                                    label='IP adres',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#AB.ipAdres',
                                    definitie='IP adres eigenschap voor legacy objecten',
                                    owner=self)

    @property
    def ipAdres(self):
        """IP adres eigenschap voor legacy objecten"""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

