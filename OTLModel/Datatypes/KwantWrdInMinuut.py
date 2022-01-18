# coding=utf-8
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMinuutEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMinuut.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in minuten.',
                                              constraints='"min"^^cdt:ucumunit',
                                              usagenote='"min"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMinuut(NonNegIntegerField, KwantWrd):
    naam = 'KwantWrdInMinuut'
    label = 'Kwantitatieve waarde in minuten'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMinuut'
    definition = 'Een kwantitatieve waarde die een getal in minuten uitdrukt.'
    eenheid = KwantWrdInMinuutEenheid()

