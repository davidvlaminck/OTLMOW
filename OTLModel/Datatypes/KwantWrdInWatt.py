# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInWattEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in Watt.',
                                              constraints='"W"^^cdt:ucumunit',
                                              usagenote='"W"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInWatt(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInWatt'
    label = 'Kwantitatieve waarde in watt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInWatt'
    definition = 'Een kwantitatieve waarde die een getal in watt uitdrukt.'
    eenheid = KwantWrdInWattEenheid()

