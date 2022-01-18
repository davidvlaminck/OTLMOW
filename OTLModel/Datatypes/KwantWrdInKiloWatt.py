# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloWattEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloWatt.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in kilowatt.',
                                              constraints='"kW"^^cdt:ucumunit',
                                              usagenote='"kW"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInKiloWatt(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInKiloWatt'
    label = 'Kwantitatieve waarde in kilowatt'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInKiloWatt'
    definition = 'Een kwantitatieve waarde die een getal in kilowatt uitdrukt.'
    eenheid = KwantWrdInKiloWattEenheid()

