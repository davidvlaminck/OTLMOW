from abc import abstractmethod
from OTLModel.Classes.Draagconstructie import Draagconstructie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlEMDraagconstructieElekBeveiliging import KlEMDraagconstructieElekBeveiliging


# Generated with OTLClassCreator. To modify: extend, do not edit
class EMDraagconstructie(Draagconstructie):
    """Abstracte voor een elektromechanisch (EM) dragend element (bv. paal, kolom, seinbrug, galgpaal) waaraan EM-toestellen bevestigd kunnen worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.elektrischeBeveiliging = KeuzelijstField(naam="elektrischeBeveiliging",
                                                      label="elektrische beveiliging",
                                                      lijst=KlEMDraagconstructieElekBeveiliging(),
                                                      uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#EMDraagconstructie.elektrischeBeveiliging",
                                                      definition="Type elektrische beveiliging aanwezig in de draagconstructie.",
                                                      constraints="",
                                                      usagenote="",
                                                      deprecated_version="")
        """Type elektrische beveiliging aanwezig in de draagconstructie."""
