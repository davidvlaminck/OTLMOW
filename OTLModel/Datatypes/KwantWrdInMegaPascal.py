# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMegaPascalEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMegaPascal.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in mega pascal.',
                                              constraints='"MPa"^^cdt:ucumunit',
                                              usagenote='"MPa"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMegaPascal(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInMegaPascal'
    label = 'Kwantitatieve waarde in MPa'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMegaPascal'
    definition = 'Een kwantitatieve waarde die een getal in megapascal uitdrukt.'
    eenheid = KwantWrdInMegaPascalEenheid()

