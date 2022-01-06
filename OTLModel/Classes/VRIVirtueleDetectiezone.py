from OTLModel.Classes.Detectielus import Detectielus
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVriLusFunctie import KlVriLusFunctie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VRIVirtueleDetectiezone(Detectielus):
    """Een virtuele detectiezone is een draadloos alternatief voor een traditionele lus. Op basis van GPS gegevens wordt een zone of traject vastgelegd waarbinnen er (al dan niet selectieve) input dient geleverd te worden aan de verkeersregelaar. De virtuele detectiezone kan ook gebruikt worden om de detectiezones van detectiecamera's en radars te inventariseren.
"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.functie = KeuzelijstField(naam="functie",
                                       label="functie",
                                       lijst=KlVriLusFunctie(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VRIVirtueleDetectiezone.functie",
                                       definition="Functie van de VRI detectiezone.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Functie van de VRI detectiezone."""
