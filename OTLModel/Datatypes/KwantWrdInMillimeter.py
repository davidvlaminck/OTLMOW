# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMillimeterEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMillimeter.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in millimeter.',
                                              constraints='"mm"^^cdt:ucumunit',
                                              usagenote='"mm"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInMillimeter(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInMillimeter'
    label = 'Kwantitatieve waarde in millimeter'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInMillimeter'
    definition = 'Een kwantitatieve waarde die een getal in millimeter uitdrukt.'
    eenheid = KwantWrdInMillimeterEenheid()

