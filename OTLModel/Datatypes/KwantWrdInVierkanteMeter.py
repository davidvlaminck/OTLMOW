# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in vierkante meter.',
                                              constraints='"m2"^^cdt:ucumunit',
                                              usagenote='"m2"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInVierkanteMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInVierkanteMeter'
    label = 'Kwantitatieve waarde in vierkante meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInVierkanteMeter'
    definition = 'Een kwantitatieve waarde die een getal in vierkante meter uitdrukt.'
    eenheid = KwantWrdInVierkanteMeterEenheid()

