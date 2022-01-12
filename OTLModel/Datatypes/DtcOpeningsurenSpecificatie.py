# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgWeekdagen import KlAlgWeekdagen
from OTLModel.Datatypes.TimeField import TimeField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcOpeningsurenSpecificatie(ComplexField):
    """Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert."""

    def __init__(self):
        super().__init__(naam="DtcOpeningsurenSpecificatie",
                         label="Openingsurenspecificatie",
                         objectUri="https://schema.org/OpeningHoursSpecification",
                         definition="Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.openingstijd = TimeField(naam="openingstijd",
                                             label="openingstijd",
                                             objectUri="https://schema.org/OpeningHoursSpecification.openingstijd",
                                             definition="Het tijdsstip waarop de opening plaatsvindt.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.openingstijd = self.waarde.openingstijd
        """Het tijdsstip waarop de opening plaatsvindt."""

        self.waarde.sluitingstijd = TimeField(naam="sluitingstijd",
                                              label="sluitingstijd",
                                              objectUri="https://schema.org/OpeningHoursSpecification.sluitingstijd",
                                              definition="Het tijdsstip waarop de sluiting plaatsvindt.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.sluitingstijd = self.waarde.sluitingstijd
        """Het tijdsstip waarop de sluiting plaatsvindt."""

        self.waarde.weekdag = KeuzelijstField(naam="weekdag",
                                              label="weekdag",
                                              lijst=KlAlgWeekdagen(),
                                              objectUri="https://schema.org/OpeningHoursSpecification.weekdag",
                                              definition="Een dag uit de week incl. weekenddagen.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.weekdag = self.waarde.weekdag
        """Een dag uit de week incl. weekenddagen."""
