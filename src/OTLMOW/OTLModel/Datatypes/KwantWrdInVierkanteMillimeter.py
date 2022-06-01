# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMillimeterWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMillimeter.standaardEenheid',
                                              usagenote='"mm4"^^cdt:ucumunit',
                                              constraints='"mm2"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in vierkante milimeter.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMillimeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in vierkante milimeter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMillimeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in vierkante millimeters uitdrukt."""
    naam = 'KwantWrdInVierkanteMillimeter'
    label = 'Kwantitatieve waarde in vierkante millimeters'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMillimeter'
    definition = 'Een kwantitatieve waarde die een getal in vierkante millimeters uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInVierkanteMillimeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

