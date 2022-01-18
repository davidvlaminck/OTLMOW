# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCelsiusEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCelsius.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in celsius.',
                                              constraints='"Cel"^^cdt:ucumunit',
                                              usagenote='"Cel"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCelsius(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInCelsius'
    label = 'Kwantitatieve waarde in Celsius'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCelsius'
    definition = 'Een kwantitatieve waarde die een getal in graden celsius uitdrukt.'
    eenheid = KwantWrdInCelsiusEenheid()

