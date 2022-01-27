# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerVierkanteMeterWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter.standaardEenheid',
                                              usagenote='"kN/m2"^^cdt:ucumunit',
                                              constraints='"kN/m2"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in KiloNewton per vierkante meter.')

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in KiloNewton per vierkante meter."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerVierkanteMeter(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in KiloNewton per vierkante meter uitdrukt."""
    naam = 'KwantWrdInKiloNewtonPerVierkanteMeter'
    label = 'Kwantitatieve waarde in kN per vierkante meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter'
    definition = 'Een kwantitatieve waarde die een getal in KiloNewton per vierkante meter uitdrukt.'
    waardeObject = KwantWrdInKiloNewtonPerVierkanteMeterWaarden

    def __str__(self):
        return OTLField.__str__(self)

