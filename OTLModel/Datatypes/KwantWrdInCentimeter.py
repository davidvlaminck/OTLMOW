# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCentimeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in centimeter.',
                                              constraints='"cm"^^cdt:ucumunit',
                                              usagenote='"cm"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInCentimeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInCentimeter'
    label = 'Kwantitatieve waarde in centimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInCentimeter'
    definition = 'Een kwantitatieve waarde die een getal in centimeter uitdrukt.'
    eenheid = KwantWrdInCentimeterEenheid()

