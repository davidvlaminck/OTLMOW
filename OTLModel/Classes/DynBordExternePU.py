from OTLModel.Classes.PU import PU
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordExternePUMerk import KlDynBordExternePUMerk
from OTLModel.Datatypes.KlDynBordExternePUModelnaam import KlDynBordExternePUModelnaam


# Generated with OTLClassCreator
class DynBordExternePU(PU):
    """Externe stuureenheid die buiten het dynamisch bord bevestigd is, in de buurt van de openbare weg. Het betreft dus geen stuureenheid in een serverroom, noch een stuureenheid op het bord zelf."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.heeftGeintegreerdeModem = BooleanField(naam="heeftGeintegreerdeModem",
                                                    label="heeft geintegreerde modem",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.heeftGeintegreerdeModem",
                                                    definition="De PU heeft een geïntegreerde modem.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """De PU heeft een geïntegreerde modem."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordExternePUMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.merk",
                                    definition="Het merk van de externe PU volgens een keuzelijst.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de externe PU volgens een keuzelijst."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordExternePUModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.modelnaam",
                                         definition="De modelnaam van de externe PU volgens een keuzelijst.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de externe PU volgens een keuzelijst."""

        self.technischeFiche = DtcDocument()
        """Document met technische informatie over de PU."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordExternePU.technischeFiche"
        self.technischeFiche.definition = "Document met technische informatie over de PU."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
