# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.KlAlgWeekdagen import KlAlgWeekdagen
from OTLMOW.OTLModel.Datatypes.TimeField import TimeField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOpeningsurenSpecificatieWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._openingstijd = OTLAttribuut(field=TimeField,
                                          naam='openingstijd',
                                          label='openingstijd',
                                          objectUri='https://schema.org/OpeningHoursSpecification.openingstijd',
                                          definition='Het tijdsstip waarop de opening plaatsvindt.',
                                          owner=self)

        self._sluitingstijd = OTLAttribuut(field=TimeField,
                                           naam='sluitingstijd',
                                           label='sluitingstijd',
                                           objectUri='https://schema.org/OpeningHoursSpecification.sluitingstijd',
                                           definition='Het tijdsstip waarop de sluiting plaatsvindt.',
                                           owner=self)

        self._weekdag = OTLAttribuut(field=KlAlgWeekdagen,
                                     naam='weekdag',
                                     label='weekdag',
                                     objectUri='https://schema.org/OpeningHoursSpecification.weekdag',
                                     definition='Een dag uit de week incl. weekenddagen.',
                                     owner=self)

    @property
    def openingstijd(self):
        """Het tijdsstip waarop de opening plaatsvindt."""
        return self._openingstijd.waarde

    @openingstijd.setter
    def openingstijd(self, value):
        self._openingstijd.set_waarde(value, owner=self._parent)

    @property
    def sluitingstijd(self):
        """Het tijdsstip waarop de sluiting plaatsvindt."""
        return self._sluitingstijd.waarde

    @sluitingstijd.setter
    def sluitingstijd(self, value):
        self._sluitingstijd.set_waarde(value, owner=self._parent)

    @property
    def weekdag(self):
        """Een dag uit de week incl. weekenddagen."""
        return self._weekdag.waarde

    @weekdag.setter
    def weekdag(self, value):
        self._weekdag.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOpeningsurenSpecificatie(ComplexField, AttributeInfo):
    """Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert."""
    naam = 'DtcOpeningsurenSpecificatie'
    label = 'Openingsurenspecificatie'
    objectUri = 'https://schema.org/OpeningHoursSpecification'
    definition = 'Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert.'
    waardeObject = DtcOpeningsurenSpecificatieWaarden

    def __str__(self):
        return ComplexField.__str__(self)

