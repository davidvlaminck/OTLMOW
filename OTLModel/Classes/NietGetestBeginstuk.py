# coding=utf-8
from OTLModel.Classes.Beginstuk import Beginstuk
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACUitbuigingstype import KlLEACUitbuigingstype


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietGetestBeginstuk(Beginstuk):
    """Een niet-gecertificeerd begin aan een geleideconstructie, aan de stroomopwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.uitbuigingstype = KeuzelijstField(naam="uitbuigingstype",
                                               label="uitbuigingstype",
                                               lijst=KlLEACUitbuigingstype(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietGetestBeginstuk.uitbuigingstype",
                                               definition="Niet getest beginstuk dat uitbuigt weg van de weg in grondplan.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Niet getest beginstuk dat uitbuigt weg van de weg in grondplan."""
