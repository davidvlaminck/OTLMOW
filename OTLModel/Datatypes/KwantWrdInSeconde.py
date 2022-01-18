# coding=utf-8
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInSecondeEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in seconde.',
                                              constraints='"s"^^cdt:ucumunit',
                                              usagenote='"s"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInSeconde(NonNegIntegerField, KwantWrd):
    naam = 'KwantWrdInSeconde'
    label = 'Kwantitatieve waarde in seconde'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInSeconde'
    definition = 'Een kwantitatieve waarde die een getal in seconde uitdrukt.'
    eenheid = KwantWrdInSecondeEenheid()

