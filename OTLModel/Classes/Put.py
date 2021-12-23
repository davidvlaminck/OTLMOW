from abc import abstractmethod, ABC
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcAdres import DtcAdres
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW


# Generated with OTLClassCreator
class Put(ABC):
    """Abstracte bedoeld om de verschillende soort putten onder te brengen en gemeenschappelijke eigenschappen over te dragen. De relaties worden overgedragen via de abstracte PutRelaties."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.adres = DtcAdres()
        """Dichtstbijgelegen adres voor de put, het adres bestaat enkel uit de straatnaam indien het dichtstbijzijnde adres > 100m verwijderd is."""
        self.adres.naam = "adres"
        self.adres.label = "adres"
        self.adres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put.adres"
        self.adres.definition = "Dichtstbijgelegen adres voor de put, het adres bestaat enkel uit de straatnaam indien het dichtstbijzijnde adres > 100m verwijderd is."
        self.adres.constraints = ""
        self.adres.usagenote = ""
        self.adres.deprecated_version = ""

        self.diepte = KwantWrdInMeter()
        """Het verschil tussen het maaiveldpeil en het laagste punt van de binnenkant van de put in meter."""
        self.diepte.naam = "diepte"
        self.diepte.label = "diepte"
        self.diepte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put.diepte"
        self.diepte.definition = "Het verschil tussen het maaiveldpeil en het laagste punt van de binnenkant van de put in meter."
        self.diepte.constraints = ""
        self.diepte.usagenote = ""
        self.diepte.deprecated_version = ""

        self.maaiveldpeil = KwantWrdInMeterTAW()
        """De hoogte van het grondoppervlak in meter-TAW in het midden van het deksel van de put."""
        self.maaiveldpeil.naam = "maaiveldpeil"
        self.maaiveldpeil.label = "maaiveldpeil"
        self.maaiveldpeil.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put.maaiveldpeil"
        self.maaiveldpeil.definition = "De hoogte van het grondoppervlak in meter-TAW in het midden van het deksel van de put."
        self.maaiveldpeil.constraints = ""
        self.maaiveldpeil.usagenote = ""
        self.maaiveldpeil.deprecated_version = ""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de put."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de put."""

        self.toestandPut = DteTekstblok()
        """Opmerkingen van de toestand en staat van de (verbindings-)put."""
        self.toestandPut.naam = "toestandPut"
        self.toestandPut.label = "toestand put"
        self.toestandPut.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Put.toestandPut"
        self.toestandPut.definition = "Opmerkingen van de toestand en staat van de (verbindings-)put."
        self.toestandPut.constraints = ""
        self.toestandPut.usagenote = ""
        self.toestandPut.deprecated_version = ""
