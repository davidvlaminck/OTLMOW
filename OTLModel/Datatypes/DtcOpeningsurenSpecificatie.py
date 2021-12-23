from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgWeekdagen import KlAlgWeekdagen
from OTLModel.Datatypes.TimeField import TimeField


# Generated with OTLComplexDatatypeCreator
class DtcOpeningsurenSpecificatie(ComplexField):
    """Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert."""

    def __init__(self):
        super().__init__(naam="DtcOpeningsurenSpecificatie",
                         label="Openingsurenspecificatie",
                         uri="https://schema.org/OpeningHoursSpecification",
                         definition="Complex datatype dat de openingsuren volgens https://schema.org/OpeningHoursSpecification specifieert.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.openingstijd = TimeField(naam="openingstijd",
                                             label="openingstijd",
                                             uri="https://schema.org/OpeningHoursSpecification.openingstijd",
                                             definition="Het tijdsstip waarop de opening plaatsvindt.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.openingstijd = self.waarde.openingstijd
        """Het tijdsstip waarop de opening plaatsvindt."""

        self.waarde.sluitingstijd = TimeField(naam="sluitingstijd",
                                              label="sluitingstijd",
                                              uri="https://schema.org/OpeningHoursSpecification.sluitingstijd",
                                              definition="Het tijdsstip waarop de sluiting plaatsvindt.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.sluitingstijd = self.waarde.sluitingstijd
        """Het tijdsstip waarop de sluiting plaatsvindt."""

        self.waarde.weekdag = KeuzelijstField(naam="weekdag",
                                              label="weekdag",
                                              lijst=KlAlgWeekdagen(),
                                              uri="https://schema.org/OpeningHoursSpecification.weekdag",
                                              definition="Een dag uit de week incl. weekenddagen.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.weekdag = self.waarde.weekdag
        """Een dag uit de week incl. weekenddagen."""
