# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLField import OTLField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInJaarWaarden(AttributeInfo):
    def __init__(self):
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar.standaardEenheid',
                                              usagenote='"a"^^cdt:ucumunit',
                                              constraints='"a"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in jaar.')

        self._waarde = OTLAttribuut(field=NonNegIntegerField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in jaar."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInJaar(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in aantal jaar uitdrukt."""
    naam = 'KwantWrdInJaar'
    label = 'Kwantitatieve waarde in aantal jaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar'
    definition = 'Een kwantitatieve waarde die een getal in aantal jaar uitdrukt.'
    waardeObject = KwantWrdInJaarWaarden

    def __str__(self):
        return OTLField.__str__(self)

