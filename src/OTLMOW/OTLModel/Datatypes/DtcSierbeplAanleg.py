# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlAanplantingswijzeSierbeplanting import KlAanplantingswijzeSierbeplanting
from OTLMOW.OTLModel.Datatypes.KlSierbeplContainer import KlSierbeplContainer
from OTLMOW.OTLModel.Datatypes.KlSierbeplPlantmaat import KlSierbeplPlantmaat
from OTLMOW.OTLModel.Datatypes.KlVegetatiePlantverband import KlVegetatiePlantverband
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSierbeplAanlegWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._aanplantingswijze = OTLAttribuut(field=KlAanplantingswijzeSierbeplanting,
                                               naam='aanplantingswijze',
                                               label='aanplantingswijze',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.aanplantingswijze',
                                               definition='Manier van aanplanten.',
                                               owner=self)

        self._containermaat = OTLAttribuut(field=KlSierbeplContainer,
                                           naam='containermaat',
                                           label='containermaat',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.containermaat',
                                           definition='De grootte van de pot of container waarin de plant wordt geleverd. De P staat voor pot, de C voor container. Het getal geeft de grootte weer in centimeter.',
                                           owner=self)

        self._plantdichtheid = OTLAttribuut(field=NonNegIntegerField,
                                            naam='plantdichtheid',
                                            label='plantdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantdichtheid',
                                            definition='Aantal planten per vierkante meter.',
                                            owner=self)

        self._plantmaat = OTLAttribuut(field=KlSierbeplPlantmaat,
                                       naam='plantmaat',
                                       label='plantmaat',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantmaat',
                                       definition='De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde.',
                                       owner=self)

        self._plantverband = OTLAttribuut(field=KlVegetatiePlantverband,
                                          naam='plantverband',
                                          label='plantverband',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg.plantverband',
                                          definition='De wijze waarop de planten zijn geschikt.',
                                          owner=self)

    @property
    def aanplantingswijze(self):
        """Manier van aanplanten."""
        return self._aanplantingswijze.get_waarde()

    @aanplantingswijze.setter
    def aanplantingswijze(self, value):
        self._aanplantingswijze.set_waarde(value, owner=self._parent)

    @property
    def containermaat(self):
        """De grootte van de pot of container waarin de plant wordt geleverd. De P staat voor pot, de C voor container. Het getal geeft de grootte weer in centimeter."""
        return self._containermaat.get_waarde()

    @containermaat.setter
    def containermaat(self, value):
        self._containermaat.set_waarde(value, owner=self._parent)

    @property
    def plantdichtheid(self):
        """Aantal planten per vierkante meter."""
        return self._plantdichtheid.get_waarde()

    @plantdichtheid.setter
    def plantdichtheid(self, value):
        self._plantdichtheid.set_waarde(value, owner=self._parent)

    @property
    def plantmaat(self):
        """De hoogte van de plant in cm gemeten tussen een minimum en maximum waarde."""
        return self._plantmaat.get_waarde()

    @plantmaat.setter
    def plantmaat(self, value):
        self._plantmaat.set_waarde(value, owner=self._parent)

    @property
    def plantverband(self):
        """De wijze waarop de planten zijn geschikt."""
        return self._plantverband.get_waarde()

    @plantverband.setter
    def plantverband(self, value):
        self._plantverband.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcSierbeplAanleg(ComplexField, AttributeInfo):
    """Complex datatype voor dat de aanleg van sierbeplanting beschrijft."""
    naam = 'DtcSierbeplAanleg'
    label = 'Sierbeplanting aanleg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DtcSierbeplAanleg'
    definition = 'Complex datatype voor dat de aanleg van sierbeplanting beschrijft.'
    waardeObject = DtcSierbeplAanlegWaarden

    def __str__(self):
        return ComplexField.__str__(self)

