# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogramPerKubiekeMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kilogram per kubieke meter.',
                                              constraints='"kg/m3"^^cdt:ucumunit',
                                              usagenote='"kg/m3"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKilogramPerKubiekeMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKilogramPerKubiekeMeter'
    label = 'Kwantitatieve waarde in kilogram per kubieke meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKilogramPerKubiekeMeter'
    definition = 'Een kwantitatieve waarde die een getal in kilogram per kubieke meter uitdrukt.'
    eenheid = KwantWrdInKilogramPerKubiekeMeterEenheid()

