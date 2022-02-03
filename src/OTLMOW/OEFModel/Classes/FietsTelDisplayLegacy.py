# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OEFClassCreator. To modify: extend, do not edit
class FietsTelDisplayLegacy(EMObject):
    """FietstelDisplay"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#FietsTelDisplayLegacy'
    label = 'Fietsteldisplay (Legacy)'

    def __init__(self):
        super().__init__()

        self._isdubbelzijdig = EMAttribuut(field=BooleanField,
                                           naam='isDubbelzijdig',
                                           label='isDubbelzijdig',
                                           objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#FietsTelDisplayLegacy.isdubbelzijdig',
                                           definitie='isDubbelzijdig',
                                           owner=self)

    @property
    def isdubbelzijdig(self):
        """isDubbelzijdig"""
        return self._isdubbelzijdig.waarde

    @isdubbelzijdig.setter
    def isdubbelzijdig(self, value):
        self._isdubbelzijdig.set_waarde(value, owner=self)

