# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInEuroWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro.standaardEenheid',
                                              usagenote='"{Euro}"^^cdt:ucumunit',
                                              constraints='"{Euro}"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in Euro.',
                                              owner=self)

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.',
                                    owner=self)

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in Euro."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.get_waarde()

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInEuro(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in Euro uitdrukt."""
    naam = 'KwantWrdInEuro'
    label = 'Kwantitatieve waarde in euro'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro'
    definition = 'Een kwantitatieve waarde die een getal in Euro uitdrukt.'
    waarde_shortcut_applicable = True
    waardeObject = KwantWrdInEuroWaarden

    def __str__(self):
        return OTLField.__str__(self)

