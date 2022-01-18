# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInPromilleEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInPromille.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in promille.',
                                              constraints='"‰"^^cdt:ucumunit',
                                              usagenote='"‰"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInPromille(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInPromille'
    label = 'Kwantitatieve waarde in promille'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInPromille'
    definition = 'Een kwantitatieve waarde die een getal in promille uitdrukt.'
    eenheid = KwantWrdInPromilleEenheid()

