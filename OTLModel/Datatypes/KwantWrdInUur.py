# coding=utf-8
from OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInUurEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInUur.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in uur.',
                                              constraints='"h"^^cdt:ucumunit',
                                              usagenote='"h"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInUur(NonNegIntegerField, KwantWrd):
    naam = 'KwantWrdInUur'
    label = 'Kwantitatieve waarde in uur'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInUur'
    definition = 'Een kwantitatieve waarde die een getal in uur uitdrukt.'
    eenheid = KwantWrdInUurEenheid()

