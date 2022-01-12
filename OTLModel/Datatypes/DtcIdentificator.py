# coding=utf-8
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcIdentificator(ComplexField):
    """Complex datatype voor de identificator van een AIM object volgens de bron van de identificator."""

    def __init__(self):
        super().__init__(naam="DtcIdentificator",
                         label="Identificator",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator",
                         definition="Complex datatype voor de identificator van een AIM object volgens de bron van de identificator.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.identificator = StringField(naam="identificator",
                                                label="identificator",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.identificator",
                                                definition="Een groep van tekens om een AIM object te identificeren of te benoemen.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.identificator = self.waarde.identificator
        """Een groep van tekens om een AIM object te identificeren of te benoemen."""

        self.waarde.toegekendDoor = StringField(naam="toegekendDoor",
                                                label="toegekend door",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcIdentificator.toegekendDoor",
                                                definition="Gegevens van de organisatie die de toekenning deed.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.toegekendDoor = self.waarde.toegekendDoor
        """Gegevens van de organisatie die de toekenning deed."""
