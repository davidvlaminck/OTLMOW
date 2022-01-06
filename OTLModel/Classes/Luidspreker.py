# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KLLuidsprekerVormgeving import KLLuidsprekerVormgeving
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLModel.Datatypes.KlLuidsprekerMerk import KlLuidsprekerMerk
from OTLModel.Datatypes.KlLuidsprekerModelnaam import KlLuidsprekerModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luidspreker(AIMNaamObject):
    """Een luidspreker is een apparaat waarmee elektrische signalen worden omgezet in geluid."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlLuidsprekerMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.merk",
                                    definition="Het merk van de luidspreker.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de luidspreker."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlLuidsprekerModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.modelnaam",
                                         definition="De modelnaam van de luidspreker.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de luidspreker."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de luidspreker."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de luidspreker."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""

        self.transportType = KeuzelijstField(naam="transportType",
                                             label="transport type",
                                             lijst=KlAudioTransportType(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.transportType",
                                             definition="Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""

        self.vormgeving = KeuzelijstField(naam="vormgeving",
                                          label="vormgeving",
                                          lijst=KLLuidsprekerVormgeving(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.vormgeving",
                                          definition="Soort luidsprekers volgens zijn vormfactor.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Soort luidsprekers volgens zijn vormfactor."""
