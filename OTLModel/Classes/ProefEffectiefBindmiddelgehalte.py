# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefEffectiefBindmiddelgehalte(Proef):
    """Bepaling van de hoeveelheid bitumen, uitgedrukt t.o.v. het totale mengsel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.effectiefBindmiddelgehalte = DtcDocument()
        """Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag."""
        self.effectiefBindmiddelgehalte.naam = "effectiefBindmiddelgehalte"
        self.effectiefBindmiddelgehalte.label = "effectief bindmiddelgehalte"
        self.effectiefBindmiddelgehalte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefEffectiefBindmiddelgehalte.effectiefBindmiddelgehalte"
        self.effectiefBindmiddelgehalte.definition = "Het resultaat van de test van het gemeten effectief bindmiddelgehalte in de BV laag."
        self.effectiefBindmiddelgehalte.constraints = ""
        self.effectiefBindmiddelgehalte.usagenote = ""
        self.effectiefBindmiddelgehalte.deprecated_version = ""
