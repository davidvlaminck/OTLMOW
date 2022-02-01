# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OEFClassCreator. To modify: extend, do not edit
class SegC(EMObject):
    """Controller die zorgt voor de bewaking en bediening van verlichtingssegmenten per paal en aldus zorgt voor de communicatie tussen de cabine en de armatuurcontrollers."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SegC'
    label = 'Segment controller'

    def __init__(self):
        super().__init__()

        self._ipAdres = EMAttribuut(field=StringField,
                                    naam='IP-adres',
                                    label='IP adres',
                                    objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#AB.ipAdres',
                                    definitie='IP adres eigenschap voor legacy objecten')

        self._merkEnTypeSegmentController = EMAttribuut(field=StringField,
                                                        naam='merk en type segment controller',
                                                        label='merk en type segment controller',
                                                        objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SegC.merkEnTypeSegmentController',
                                                        definitie='merk en type segment controller')

        self._serienummerSegmentController = EMAttribuut(field=StringField,
                                                         naam='serienummer segment controller',
                                                         label='serienummer segment controller',
                                                         objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#SegC.serienummerSegmentController',
                                                         definitie='serienummer segment controller')

    @property
    def ipAdres(self):
        """IP adres eigenschap voor legacy objecten"""
        return self._ipAdres.waarde

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def merkEnTypeSegmentController(self):
        """merk en type segment controller"""
        return self._merkEnTypeSegmentController.waarde

    @merkEnTypeSegmentController.setter
    def merkEnTypeSegmentController(self, value):
        self._merkEnTypeSegmentController.set_waarde(value, owner=self)

    @property
    def serienummerSegmentController(self):
        """serienummer segment controller"""
        return self._serienummerSegmentController.waarde

    @serienummerSegmentController.setter
    def serienummerSegmentController(self, value):
        self._serienummerSegmentController.set_waarde(value, owner=self)

