# coding=utf-8
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefNaderOnderzoekTomograaf(Proef):
    """Een geluids- en/of elektrische weerstandstomografie is een niet-destructieve methode om rot en holtes in bomen op te sporen door gebruik van geluidsgolven en/of elektrische stroom."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.inclusiefElektrisch = BooleanField(naam="inclusiefElektrisch",
                                                label="inclusief elektrisch",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.inclusiefElektrisch",
                                                definition="Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Aanduiding of naast een geluidsweerstandstomografie ook een elektrische weerstandstomografie gebeurd is."""

        naderOnderzoekTomograafField = DtcDocument()
        naderOnderzoekTomograafField.naam = "naderOnderzoekTomograaf"
        naderOnderzoekTomograafField.label = "nader onderzoek tomograaf"
        naderOnderzoekTomograafField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefNaderOnderzoekTomograaf.naderOnderzoekTomograaf"
        naderOnderzoekTomograafField.definition = "Het resultaat van de tomograaf proef."
        naderOnderzoekTomograafField.constraints = ""
        naderOnderzoekTomograafField.usagenote = ""
        naderOnderzoekTomograafField.deprecated_version = ""
        self.naderOnderzoekTomograaf = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=naderOnderzoekTomograafField)
        """Het resultaat van de tomograaf proef."""
