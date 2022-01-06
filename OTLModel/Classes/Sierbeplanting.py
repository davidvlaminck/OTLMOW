# coding=utf-8
from OTLModel.Classes.BegroeidVoorkomen import BegroeidVoorkomen
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcSierbeplAanleg import DtcSierbeplAanleg
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSierbeplantingType import KlSierbeplantingType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sierbeplanting(BegroeidVoorkomen):
    """Planten die geen blijvende houtige stengel vormen. Eenjarige,tweejarige of vaste planten,die in de winter tot de grond toe afsterven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aanleg = DtcSierbeplAanleg()
        """De manier van aanplanten van de sierbeplanting."""
        self.aanleg.naam = "aanleg"
        self.aanleg.label = "aanleg"
        self.aanleg.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.aanleg"
        self.aanleg.definition = "De manier van aanplanten van de sierbeplanting."
        self.aanleg.constraints = ""
        self.aanleg.usagenote = ""
        self.aanleg.deprecated_version = ""

        typeField = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlSierbeplantingType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sierbeplanting.type",
                                    definition="Type van sierbeplanting.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        self.type = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=typeField)
        """Type van sierbeplanting."""
