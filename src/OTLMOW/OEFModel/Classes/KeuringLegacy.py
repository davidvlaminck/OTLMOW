# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class KeuringLegacy(EMObject):
    """Specifiek opdrachttype : KEURING van de installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#KeuringLegacy'
    label = 'Keuring (Legacy)'

    def __init__(self):
        super().__init__()

        self._notitieKeuring = EMAttribuut(field=StringField,
                                           naam='Notitie (KEURING)',
                                           label='Notitie (KEURING)',
                                           objectUri='https://ond.data.wegenenverkeer.be/ns/attribuut#KeuringLegacy.notitieKeuring',
                                           definitie='Definitie nog toe te voegen voor eigenschap Notitie (KEURING)')

    @property
    def notitieKeuring(self):
        """Definitie nog toe te voegen voor eigenschap Notitie (KEURING)"""
        return self._notitieKeuring.waarde

    @notitieKeuring.setter
    def notitieKeuring(self, value):
        self._notitieKeuring.set_waarde(value, owner=self)

