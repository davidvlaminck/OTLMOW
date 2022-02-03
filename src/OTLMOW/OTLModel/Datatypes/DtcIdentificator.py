# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcIdentificatorWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._identificator = OTLAttribuut(field=StringField,
                                           naam='identificator',
                                           label='identificator',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator',
                                           definition='Een groep van tekens om een AIM object te identificeren of te benoemen.',
                                           owner=self)

        self._toegekendDoor = OTLAttribuut(field=StringField,
                                           naam='toegekendDoor',
                                           label='toegekend door',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor',
                                           definition='Gegevens van de organisatie die de toekenning deed.',
                                           owner=self)

    @property
    def identificator(self):
        """Een groep van tekens om een AIM object te identificeren of te benoemen."""
        return self._identificator.waarde

    @identificator.setter
    def identificator(self, value):
        self._identificator.set_waarde(value, owner=self._parent)

    @property
    def toegekendDoor(self):
        """Gegevens van de organisatie die de toekenning deed."""
        return self._toegekendDoor.waarde

    @toegekendDoor.setter
    def toegekendDoor(self, value):
        self._toegekendDoor.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcIdentificator(ComplexField, AttributeInfo):
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""
    naam = 'DtcIdentificator'
    label = 'Identificator'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator'
    definition = 'Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.'
    waardeObject = DtcIdentificatorWaarden

    def __str__(self):
        return ComplexField.__str__(self)

