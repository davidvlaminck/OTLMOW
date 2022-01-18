# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVoltAmpereEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVoltAmpere.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kiloVoltAmpere.',
                                              constraints='"kVA*"^^cdt:ucumunit',
                                              usagenote='"kVA*"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloVoltAmpere(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloVoltAmpere'
    label = 'Kwantitatieve waarde in kilovoltampère'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloVoltAmpere'
    definition = 'Een kwantitatieve waarde die een getal in kilovoltampère uitdrukt.'
    eenheid = KwantWrdInKiloVoltAmpereEenheid()

