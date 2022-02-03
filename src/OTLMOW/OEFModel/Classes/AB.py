# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class AB(EMObject):
    """Afstandsbewaking"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AB'
    label = 'Afstandsbewaking'

    def __init__(self):
        super().__init__()

        self._ipAdres = EMAttribuut(field=StringField,
                                    naam='IP-adres',
                                    label='IP adres',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#AB.ipAdres',
                                    definitie='IP adres eigenschap voor legacy objecten',
                                    owner=self)

        self._notitieinspectie = EMAttribuut(field=StringField,
                                             naam='notitieInspectie',
                                             label='notitieInspectie',
                                             objectUri='https://ins.data.wegenenverkeer.be/ns/attribuut#EMObject.notitieinspectie',
                                             definitie='Definitie nog toe te voegen voor eigenschap notitie',
                                             owner=self)

    @property
    def ipAdres(self):
        """IP adres eigenschap voor legacy objecten"""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def notitieinspectie(self):
        """Definitie nog toe te voegen voor eigenschap notitie"""
        return self._notitieinspectie.waarde

    @notitieinspectie.setter
    def notitieinspectie(self, value):
        self._notitieinspectie.set_waarde(value, owner=self)

