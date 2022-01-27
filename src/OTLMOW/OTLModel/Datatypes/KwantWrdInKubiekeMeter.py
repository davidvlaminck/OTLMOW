# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from src.OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeterWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter.standaardEenheid',
                                              usagenote='"m3"^^cdt:ucumunit',
                                              constraints='"m3"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter.')

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in kubieke meter uitdrukt."""
    naam = 'KwantWrdInKubiekeMeter'
    label = 'Kwantitatieve waarde in kubieke meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter'
    definition = 'Een kwantitatieve waarde die een getal in kubieke meter uitdrukt.'
    waardeObject = KwantWrdInKubiekeMeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

