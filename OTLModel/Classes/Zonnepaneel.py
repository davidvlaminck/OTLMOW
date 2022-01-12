# coding=utf-8
from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlZonnepaneelMerk import KlZonnepaneelMerk
from OTLModel.Datatypes.KlZonnepaneelModelnaam import KlZonnepaneelModelnaam
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zonnepaneel(Voedingspunt, BevestigingGC):
    """Toestel om elektrische energie op te wekken uit zonlicht met als doel het voeden van een installatie. Ook wel fotovoltaïsche cellen of zonnecellen genoemd."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Voedingspunt.__init__(self)
        BevestigingGC.__init__(self)

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlZonnepaneelMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.merk",
                                    definition="Het merk van het zonnepaneel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van het zonnepaneel."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlZonnepaneelModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.modelnaam",
                                         definition="De modelnaam van het zonnepaneel.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van het zonnepaneel."""

        self.vermogen = KwantWrdInWatt()
        """Het vermogen van het zonnepaneel."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zonnepaneel.vermogen"
        self.vermogen.definition = "Het vermogen van het zonnepaneel."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
