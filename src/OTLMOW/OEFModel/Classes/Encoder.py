# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class Encoder(EMObject):
    """Camera-uitrusting : Het betreft hier een video-encoder. Deze vormt een analoog videosignaal om tot een digitale datastroom"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Encoder'
    label = 'Encoder'

    def __init__(self):
        super().__init__()

        self._datumNieuweEncoder = EMAttribuut(field=DateField,
                                               naam='datum nieuwe encoder',
                                               label='datum nieuwe encoder',
                                               objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.datumNieuweEncoder',
                                               definitie='Definitie nog toe te voegen voor eigenschap datum nieuwe encoder')

        self._merkEnTypeEncoder = EMAttribuut(field=StringField,
                                              naam='merk en type encoder',
                                              label='merk en type encoder',
                                              objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#Encoder.merkEnTypeEncoder',
                                              definitie='Definitie nog toe te voegen voor eigenschap merk en type encoder')

    @property
    def datumNieuweEncoder(self):
        """Definitie nog toe te voegen voor eigenschap datum nieuwe encoder"""
        return self._datumNieuweEncoder.waarde

    @datumNieuweEncoder.setter
    def datumNieuweEncoder(self, value):
        self._datumNieuweEncoder.set_waarde(value, owner=self)

    @property
    def merkEnTypeEncoder(self):
        """Definitie nog toe te voegen voor eigenschap merk en type encoder"""
        return self._merkEnTypeEncoder.waarde

    @merkEnTypeEncoder.setter
    def merkEnTypeEncoder(self, value):
        self._merkEnTypeEncoder.set_waarde(value, owner=self)

