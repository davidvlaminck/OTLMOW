# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCoordLambert72Waarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._xcoordinaat = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='xcoordinaat',
                                         label='x-coördinaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCoordLambert72.xcoordinaat',
                                         definition='X-coordinaat in decimaal getal.',
                                         owner=self)

        self._ycoordinaat = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='ycoordinaat',
                                         label='y-coördinaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCoordLambert72.ycoordinaat',
                                         definition='Y-coordinaat in decimaal getal.',
                                         owner=self)

        self._zcoordinaat = OTLAttribuut(field=KwantWrdInMeterTAW,
                                         naam='zcoordinaat',
                                         label='z-coördinaat',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCoordLambert72.zcoordinaat',
                                         definition='Z-coordinaat tov. het TAW-peil in decimaal getal.',
                                         owner=self)

    @property
    def xcoordinaat(self):
        """X-coordinaat in decimaal getal."""
        return self._xcoordinaat.get_waarde()

    @xcoordinaat.setter
    def xcoordinaat(self, value):
        self._xcoordinaat.set_waarde(value, owner=self._parent)

    @property
    def ycoordinaat(self):
        """Y-coordinaat in decimaal getal."""
        return self._ycoordinaat.get_waarde()

    @ycoordinaat.setter
    def ycoordinaat(self, value):
        self._ycoordinaat.set_waarde(value, owner=self._parent)

    @property
    def zcoordinaat(self):
        """Z-coordinaat tov. het TAW-peil in decimaal getal."""
        return self._zcoordinaat.get_waarde()

    @zcoordinaat.setter
    def zcoordinaat(self, value):
        self._zcoordinaat.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCoordLambert72(ComplexField, AttributeInfo):
    """Complex datatype, beschrijft een locatie volgens het Lambert72 coördinatenstelsel."""
    naam = 'DtcCoordLambert72'
    label = 'Coördinaat Lambert72'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCoordLambert72'
    definition = 'Complex datatype, beschrijft een locatie volgens het Lambert72 coördinatenstelsel.'
    waardeObject = DtcCoordLambert72Waarden

    def __str__(self):
        return ComplexField.__str__(self)

