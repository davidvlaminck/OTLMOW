# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMilliAmpereEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in milliAmpere.',
                                              constraints='"mA"^^cdt:ucumunit',
                                              usagenote='"mA"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMilliAmpere(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInMilliAmpere'
    label = 'Kwantitatieve waarde in milliampère'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMilliAmpere'
    definition = 'Een kwantitatieve waarde die een getal in milliampère uitdrukt.'
    eenheid = KwantWrdInMilliAmpereEenheid()

