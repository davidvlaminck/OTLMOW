# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInDecimaleGradenEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInDecimaleGraden.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in decimale graden.',
                                              constraints='"deg"^^cdt:ucumunit',
                                              usagenote='"deg"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInDecimaleGraden(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInDecimaleGraden'
    label = 'Kwantitatieve waarde in decimale graden'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInDecimaleGraden'
    definition = 'Een kwantitatieve waarde die een getal in decimale graden uitdrukt.'
    eenheid = KwantWrdInDecimaleGradenEenheid()

