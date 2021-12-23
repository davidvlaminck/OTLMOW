from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp


# Generated with OTLClassCreator
class Aanstraalverlichting(AIMObject):
    """Lamp met fel gebundeld licht die het verlicht gebied duidelijk zichtbaar maakt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlBinnenverlichtingstoestelSoortLamp(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting.type",
                                    definition="Geeft het soort lamp mee dat voor de verlichting zorgt.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Geeft het soort lamp mee dat voor de verlichting zorgt."""
