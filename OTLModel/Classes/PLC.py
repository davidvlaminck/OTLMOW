from OTLModel.Classes.Controller import Controller
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPLCMerk import KlPLCMerk
from OTLModel.Datatypes.KlPLCModelnaam import KlPLCModelnaam


# Generated with OTLClassCreator
class PLC(Controller):
    """Een verwerkingseenheid die volgens een vaste cyclus op basis van informatie van zijn ingangen, zijn uitgangen aanstuurt op basis van zijn programma. Omwille van zijn vormfactor kan de eenheid gebruikt worden in een vijandige omgeving."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPLCMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.merk",
                                    definition="Het merk van de PLC.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de PLC."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPLCModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.modelnaam",
                                         definition="De modelnaam van de PLC.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de PLC."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de PLC."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technischeFiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PLC.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de PLC."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
