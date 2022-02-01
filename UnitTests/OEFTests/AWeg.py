# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class AID(EMObject):
    """Automatische incidentendetectie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AID'
    label = 'Automatische incidentendetectie'

    def __init__(self):
        super().__init__()

        self._encoderAanwezig = EMAttribuut(field=BooleanField,
                                            naam='encoder aanwezig?',
                                            label='encoder aanwezig?',
                                            objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#EMObject.encoderAanwezig',
                                            definitie='Definitie nog toe te voegen voor eigenschap encoder aanwezig?')

    @property
    def encoderAanwezig(self):
        return self._encoderAanwezig.waarde

    @encoderAanwezig.setter
    def encoderAanwezig(self, value):
        self._encoderAanwezig.set_waarde(value, owner=self)
