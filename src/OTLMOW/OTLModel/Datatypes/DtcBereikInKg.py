# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KwantWrdInKilogram import KwantWrdInKilogram


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBereikInKgWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._maximum = OTLAttribuut(field=KwantWrdInKilogram,
                                     naam='maximum',
                                     label='maximum',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg.maximum',
                                     definition='Bovengrens van het bereik uitgedrukt in kilogram.',
                                     owner=self)

        self._minimium = OTLAttribuut(field=KwantWrdInKilogram,
                                      naam='minimium',
                                      label='minimum',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg.minimium',
                                      definition='Ondergrens van het bereik uitgedrukt in kilogram.',
                                      owner=self)

    @property
    def maximum(self):
        """Bovengrens van het bereik uitgedrukt in kilogram."""
        return self._maximum.get_waarde()

    @maximum.setter
    def maximum(self, value):
        self._maximum.set_waarde(value, owner=self._parent)

    @property
    def minimium(self):
        """Ondergrens van het bereik uitgedrukt in kilogram."""
        return self._minimium.get_waarde()

    @minimium.setter
    def minimium(self, value):
        self._minimium.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBereikInKg(ComplexField, AttributeInfo):
    """Complex datatype om een bereik uit te drukken met een minimium en maximum in kilogram."""
    naam = 'DtcBereikInKg'
    label = 'Bereik in kg'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBereikInKg'
    definition = 'Complex datatype om een bereik uit te drukken met een minimium en maximum in kilogram.'
    waardeObject = DtcBereikInKgWaarden

    def __str__(self):
        return ComplexField.__str__(self)

