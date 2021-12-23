from OTLModel.Classes.Controller import Controller
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlControllerBeveiligingssleutel import KlControllerBeveiligingssleutel
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Segmentcontroller(Controller):
    """Controller die zorgt voor de bewaking en bediening van verlichtingssegmenten per paal en aldus zorgt voor de communicatie tussen de cabine en de armatuurcontrollers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.beveiligingssleutel = KeuzelijstField(naam="beveiligingssleutel",
                                                   label="beveiligingssleutel",
                                                   lijst=KlControllerBeveiligingssleutel(),
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveiligingssleutel",
                                                   definition="De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""

        self.merk = StringField(naam="merk",
                                label="merk",
                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.merk",
                                definition="Merk van de segmentcontroller.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """Merk van de segmentcontroller."""

        self.modelnaam = StringField(naam="modelnaam",
                                     label="modelnaam",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.modelnaam",
                                     definition="Modelnaam van de segmentcontroller.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Modelnaam van de segmentcontroller."""
