# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVoltEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVolt.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kilovolt.',
                                              constraints='"kV"^^cdt:ucumunit',
                                              usagenote='"kV"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVolt(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloVolt'
    label = 'Kwantitatieve waarde in kilovolt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVolt'
    definition = 'Een kwantitatieve waarde die een getal in kilovolt uitdrukt.'
    eenheid = KwantWrdInKiloVoltEenheid()

