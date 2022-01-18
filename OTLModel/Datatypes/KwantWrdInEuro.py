# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInEuroEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in Euro.',
                                              constraints='"{Euro}"^^cdt:ucumunit',
                                              usagenote='"{Euro}"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInEuro(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInEuro'
    label = 'Kwantitatieve waarde in euro'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInEuro'
    definition = 'Een kwantitatieve waarde die een getal in Euro uitdrukt.'
    eenheid = KwantWrdInEuroEenheid()

