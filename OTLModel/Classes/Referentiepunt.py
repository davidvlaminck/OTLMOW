# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSignalisatieReferentiepuntType import KlSignalisatieReferentiepuntType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Referentiepunt(AIMObject, Signalisatie, BevestigingGC):
    """Een kilometer- of hectometerpaal."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)
        BevestigingGC.__init__(self)

        self.opschrift = DteTekstblok()
        """De notatie van het referentiepunt."""
        self.opschrift.naam = "opschrift"
        self.opschrift.label = "opschrift"
        self.opschrift.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.opschrift"
        self.opschrift.definition = "De notatie van het referentiepunt."
        self.opschrift.constraints = ""
        self.opschrift.usagenote = ""
        self.opschrift.deprecated_version = ""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlSignalisatieReferentiepuntType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Referentiepunt.type",
                                    definition="Het type van referentiepunt.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van referentiepunt."""
