# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogramPerKubiekeMeterWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter.standaardEenheid',
                                              usagenote='"kg/m3"^^cdt:ucumunit',
                                              readonly=True,
                                              constraints='"kg/m3"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kilogram per kubieke meter.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in kilogram per kubieke meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogramPerKubiekeMeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in kilogram per kubieke meter uitdrukt."""
    naam = 'KwantWrdInKilogramPerKubiekeMeter'
    label = 'Kwantitatieve waarde in kilogram per kubieke meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter'
    definition = 'Een kwantitatieve waarde die een getal in kilogram per kubieke meter uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInKilogramPerKubiekeMeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

