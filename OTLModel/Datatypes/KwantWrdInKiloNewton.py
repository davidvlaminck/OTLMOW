# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewtonEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewton.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kiloNewton.',
                                              constraints='"kN"^^cdt:ucumunit',
                                              usagenote='"kN"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloNewton(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloNewton'
    label = 'Kwantitatieve waarde in kN'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloNewton'
    definition = 'Een kwantitatieve waarde die een getal in KiloNewton uitdrukt.'
    eenheid = KwantWrdInKiloNewtonEenheid()

