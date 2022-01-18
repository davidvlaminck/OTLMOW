# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerVierkanteMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in KiloNewton per vierkante meter.',
                                              constraints='"kN/m2"^^cdt:ucumunit',
                                              usagenote='"kN/m2"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerVierkanteMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloNewtonPerVierkanteMeter'
    label = 'Kwantitatieve waarde in kN per vierkante meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerVierkanteMeter'
    definition = 'Een kwantitatieve waarde die een getal in KiloNewton per vierkante meter uitdrukt.'
    eenheid = KwantWrdInKiloNewtonPerVierkanteMeterEenheid()

