# coding=utf-8
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInJaarEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in jaar.',
                                              constraints='"a"^^cdt:ucumunit',
                                              usagenote='"a"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInJaar(NonNegIntegerField, KwantWrd):
    naam = 'KwantWrdInJaar'
    label = 'Kwantitatieve waarde in aantal jaar'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInJaar'
    definition = 'Een kwantitatieve waarde die een getal in aantal jaar uitdrukt.'
    eenheid = KwantWrdInJaarEenheid()

