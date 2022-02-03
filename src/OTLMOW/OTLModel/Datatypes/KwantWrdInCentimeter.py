# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCentimeterWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.standaardEenheid',
                                              usagenote='"cm"^^cdt:ucumunit',
                                              constraints='"cm"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in centimeter.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in centimeter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCentimeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in centimeter uitdrukt."""
    naam = 'KwantWrdInCentimeter'
    label = 'Kwantitatieve waarde in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter'
    definition = 'Een kwantitatieve waarde die een getal in centimeter uitdrukt.'
    waardeObject = KwantWrdInCentimeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

