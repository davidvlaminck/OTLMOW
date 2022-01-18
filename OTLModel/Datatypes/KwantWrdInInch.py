# coding=utf-8
from OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLModel.Datatypes.LiteralField import LiteralField
from OTLModel.BaseClasses.KwantWrd import KwantWrd
from OTLModel.BaseClasses.KwantWrdEenheid import KwantWrdEenheid
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInInchEenheid(KwantWrdEenheid):
    def __init__(self):
        super().__init__()
        self._standaardEenheid = OTLAttribuut(field=LiteralField,
                                              naam='standaardEenheid',
                                              label='standaard eenheid',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch.standaardEenheid',
                                              definition='De standaard eenheid bij dit datatype is uitgedrukt in inch als internationale eenheid (eengemaakte Britse en Amerikaanse systeem).',
                                              constraints='"[in_i]"^^cdt:ucumunit',
                                              usagenote='"[in_i]"^^cdt:ucumunit')


# Generated with OTLPrimitiveDatatypeCreator. To modify: extend, do not edit
class KwantWrdInInch(FloatOrDecimalField, KwantWrd):
    naam = 'KwantWrdInInch'
    label = 'Kwantitatieve waarde in inch'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrdInInch'
    definition = 'Een kwantitatieve waarde die een getal in inches uitdrukt.'
    eenheid = KwantWrdInInchEenheid()

