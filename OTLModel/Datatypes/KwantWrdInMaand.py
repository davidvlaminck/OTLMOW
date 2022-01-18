# coding=utf-8
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMaandEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in maand.',
                                              constraints='"mo"^^cdt:ucumunit',
                                              usagenote='"mo"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMaand(NonNegIntegerField, KwantWrd):
    naam = 'KwantWrdInMaand'
    label = 'Kwantitatieve waarde in maand'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMaand'
    definition = 'Een kwantitatieve waarde die een getal in aantal maanden uitdrukt.'
    eenheid = KwantWrdInMaandEenheid()

