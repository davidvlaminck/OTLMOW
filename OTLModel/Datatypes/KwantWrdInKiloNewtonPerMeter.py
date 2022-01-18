# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerMeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerMeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton per meter.',
                                              constraints='"kN/m"^^cdt:ucumunit',
                                              usagenote='"kN/m"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonPerMeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloNewtonPerMeter'
    label = 'Kwantitatieve waarde in kiloNewton per meter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewtonPerMeter'
    definition = 'Een kwantitatieve waarde die een getal in  kiloNewton per meter uitdrukt.'
    eenheid = KwantWrdInKiloNewtonPerMeterEenheid()

