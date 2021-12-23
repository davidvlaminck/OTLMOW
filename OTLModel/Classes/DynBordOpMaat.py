from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordOpMaatMerk import KlDynBordOpMaatMerk
from OTLModel.Datatypes.KlDynBordOpMaatModelnaam import KlDynBordOpMaatModelnaam


# Generated with OTLClassCreator
class DynBordOpMaat(LEDBord):
    """Dynamisch verkeersbord dat niet standaard is; en dus niet is gespecifieerd in SB270."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordOpMaatMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.merk",
                                    definition="Merknaam van het dynamisch bord op maat.",
                                    constraints="",
                                    usagenote="Uit een keuzelijst.",
                                    deprecated_version="")
        """Merknaam van het dynamisch bord op maat."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordOpMaatModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordOpMaat.modelnaam",
                                         definition="Modelnaam van het dynamisch bord op maat.",
                                         constraints="",
                                         usagenote="Uit een keuzelijst",
                                         deprecated_version="")
        """Modelnaam van het dynamisch bord op maat."""
