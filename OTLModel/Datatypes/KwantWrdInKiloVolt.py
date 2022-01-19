# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLField import OTLField
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVoltWaarden(AttributeInfo):
    def __init__(self):
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVolt.standaardEenheid',
                                              usagenote='"kV"^^cdt:ucumunit',
                                              constraints='"kV"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kilovolt.')

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVolt.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in kilovolt."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVolt(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in kilovolt uitdrukt."""
    naam = 'KwantWrdInKiloVolt'
    label = 'Kwantitatieve waarde in kilovolt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVolt'
    definition = 'Een kwantitatieve waarde die een getal in kilovolt uitdrukt.'
    waardeObject = KwantWrdInKiloVoltWaarden

    def __str__(self):
        return OTLField.__str__(self)

