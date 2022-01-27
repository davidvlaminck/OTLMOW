# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from src.OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInInchWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch.standaardEenheid',
                                              usagenote='"[in_i]"^^cdt:ucumunit',
                                              constraints='"[in_i]"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in inch als internationale eenheid (eengemaakte Britse en Amerikaanse systeem).')

        self._waarde = OTLAttribuut(field=FloatOrDecimalField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in inch als internationale eenheid (eengemaakte Britse en Amerikaanse systeem)."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInInch(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in inches uitdrukt."""
    naam = 'KwantWrdInInch'
    label = 'Kwantitatieve waarde in inch'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch'
    definition = 'Een kwantitatieve waarde die een getal in inches uitdrukt.'
    waardeObject = KwantWrdInInchWaarden

    def __str__(self):
        return OTLField.__str__(self)

