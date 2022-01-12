# coding=utf-8
from OTLModel.Classes.Voedingspunt import Voedingspunt
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dieselgenerator(Voedingspunt):
    """Dieselmotor die een generator (machine die mechanische energie omzet in elektrische energie) aandrijft,typisch gebruikt als noodstroom aggregaat bij het wegvallen van de normale netvoeding."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.afmetingen = DtcAfmetingBxlxhInMm()
        """De afmetingen van de dieselgenerator."""
        self.afmetingen.naam = "afmetingen"
        self.afmetingen.label = "afmetingen"
        self.afmetingen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dieselgenerator.afmetingen"
        self.afmetingen.definition = "De afmetingen van de dieselgenerator."
        self.afmetingen.constraints = ""
        self.afmetingen.usagenote = ""
        self.afmetingen.deprecated_version = ""
