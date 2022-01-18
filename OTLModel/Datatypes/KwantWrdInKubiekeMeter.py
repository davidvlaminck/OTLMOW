# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kubieke meter.',
                                              constraints='"m3"^^cdt:ucumunit',
                                              usagenote='"m3"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKubiekeMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKubiekeMeter'
    label = 'Kwantitatieve waarde in kubieke meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKubiekeMeter'
    definition = 'Een kwantitatieve waarde die een getal in kubieke meter uitdrukt.'
    eenheid = KwantWrdInKubiekeMeterEenheid()

