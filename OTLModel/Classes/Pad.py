# coding=utf-8
from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPadNetwerkprotectie import KlPadNetwerkprotectie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pad(NaampadObject):
    """Een aaneengesloten reeks van links die samen een verbinding realiseren over het netwerk, gebruik makende van eenzelfde technologie (vb SDH, OTN…)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        netwerkprotectieField = KeuzelijstField(naam="netwerkprotectie",
                                                label="netwerkprotectie",
                                                lijst=KlPadNetwerkprotectie(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Pad.netwerkprotectie",
                                                definition="Referentie van het pad dat redundantie levert aan dit pad.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        self.netwerkprotectie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=netwerkprotectieField)
        """Referentie van het pad dat redundantie levert aan dit pad."""
