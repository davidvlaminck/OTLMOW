# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeCentimeterPerMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kubieke centimeter per meter.',
                                              constraints='"cm3/m"^^cdt:ucumunit',
                                              usagenote='"cm3/m"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeCentimeterPerMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKubiekeCentimeterPerMeter'
    label = 'Kwantitatieve waarde in kubieke centimeter per meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeCentimeterPerMeter'
    definition = 'Een kwantitatieve waarde die een getal in kubieke centimeter per meter uitdrukt.'
    eenheid = KwantWrdInKubiekeCentimeterPerMeterEenheid()

