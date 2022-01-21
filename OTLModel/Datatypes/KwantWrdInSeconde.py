# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLField import OTLField
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInSecondeWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=StringField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde.standaardEenheid',
                                              usagenote='"s"^^cdt:ucumunit',
                                              constraints='"s"^^cdt:ucumunit',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in seconde.')

        self._waarde = OTLAttribuut(field=NonNegIntegerField,
                                    naam='waarde',
                                    label='waarde',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde.waarde',
                                    definition='Bevat een getal die bij het datatype hoort.')

    @property
    def standaardEenheid(self):
        """De standaard eenheid bij dit datatype is uitgedrukt in seconde."""
        return self._standaardEenheid.usagenote.split('"')[1]

    @property
    def waarde(self):
        """Bevat een getal die bij het datatype hoort."""
        return self._waarde.waarde

    @waarde.setter
    def waarde(self, value):
        self._waarde.set_waarde(value, owner=self._parent)


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInSeconde(OTLField, AttributeInfo):
    """Een kwantitatieve waarde die een getal in seconde uitdrukt."""
    naam = 'KwantWrdInSeconde'
    label = 'Kwantitatieve waarde in seconde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde'
    definition = 'Een kwantitatieve waarde die een getal in seconde uitdrukt.'
    waardeObject = KwantWrdInSecondeWaarden

    def __str__(self):
        return OTLField.__str__(self)

