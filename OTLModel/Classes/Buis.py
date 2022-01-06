from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMeterTAW import KwantWrdInMeterTAW
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLModel.Datatypes.KwantWrdInPromille import KwantWrdInPromille


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buis(AIMObject):
    """Abstracte om de gemeenschappelijke eigenschappen en relaties van de verschillende soorten buizen onder één noemer te houden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.bokAfwaarts = KwantWrdInMeterTAW()
        """Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."""
        self.bokAfwaarts.naam = "bokAfwaarts"
        self.bokAfwaarts.label = "bok afwaarts"
        self.bokAfwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokAfwaarts"
        self.bokAfwaarts.definition = "Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."
        self.bokAfwaarts.constraints = ""
        self.bokAfwaarts.usagenote = ""
        self.bokAfwaarts.deprecated_version = ""

        self.bokOpwaarts = KwantWrdInMeterTAW()
        """Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."""
        self.bokOpwaarts.naam = "bokOpwaarts"
        self.bokOpwaarts.label = "bok opwaarts"
        self.bokOpwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokOpwaarts"
        self.bokOpwaarts.definition = "Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."
        self.bokOpwaarts.constraints = ""
        self.bokOpwaarts.usagenote = ""
        self.bokOpwaarts.deprecated_version = ""

        self.breedteBinnenzijde = KwantWrdInMillimeter()
        """De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        self.breedteBinnenzijde.naam = "breedteBinnenzijde"
        self.breedteBinnenzijde.label = "breedte binnenzijde"
        self.breedteBinnenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBinnenzijde"
        self.breedteBinnenzijde.definition = "De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."
        self.breedteBinnenzijde.constraints = ""
        self.breedteBinnenzijde.usagenote = ""
        self.breedteBinnenzijde.deprecated_version = ""

        self.breedteBuitenzijde = KwantWrdInMillimeter()
        """De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        self.breedteBuitenzijde.naam = "breedteBuitenzijde"
        self.breedteBuitenzijde.label = "breedte buitenzijde"
        self.breedteBuitenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBuitenzijde"
        self.breedteBuitenzijde.definition = "De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."
        self.breedteBuitenzijde.constraints = ""
        self.breedteBuitenzijde.usagenote = ""
        self.breedteBuitenzijde.deprecated_version = ""

        self.diepteAfwaarts = KwantWrdInMeter()
        """Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        self.diepteAfwaarts.naam = "diepteAfwaarts"
        self.diepteAfwaarts.label = "diepte afwaarts"
        self.diepteAfwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteAfwaarts"
        self.diepteAfwaarts.definition = "Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."
        self.diepteAfwaarts.constraints = ""
        self.diepteAfwaarts.usagenote = ""
        self.diepteAfwaarts.deprecated_version = ""

        self.diepteOpwaarts = KwantWrdInMeter()
        """De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        self.diepteOpwaarts.naam = "diepteOpwaarts"
        self.diepteOpwaarts.label = "diepte opwaarts"
        self.diepteOpwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteOpwaarts"
        self.diepteOpwaarts.definition = "De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."
        self.diepteOpwaarts.constraints = ""
        self.diepteOpwaarts.usagenote = ""
        self.diepteOpwaarts.deprecated_version = ""

        self.helling = KwantWrdInPromille()
        """De helling van de buis in de lengterichting, uitgedrukt in promille."""
        self.helling.naam = "helling"
        self.helling.label = "helling"
        self.helling.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.helling"
        self.helling.definition = "De helling van de buis in de lengterichting, uitgedrukt in promille."
        self.helling.constraints = ""
        self.helling.usagenote = ""
        self.helling.deprecated_version = ""

        self.hoogteBinnenzijde = KwantWrdInMillimeter()
        """De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        self.hoogteBinnenzijde.naam = "hoogteBinnenzijde"
        self.hoogteBinnenzijde.label = "hoogte binnenzijde"
        self.hoogteBinnenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBinnenzijde"
        self.hoogteBinnenzijde.definition = "De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."
        self.hoogteBinnenzijde.constraints = ""
        self.hoogteBinnenzijde.usagenote = ""
        self.hoogteBinnenzijde.deprecated_version = ""

        self.hoogteBuitenzijde = KwantWrdInMillimeter()
        """De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        self.hoogteBuitenzijde.naam = "hoogteBuitenzijde"
        self.hoogteBuitenzijde.label = "hoogte buitenzijde"
        self.hoogteBuitenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBuitenzijde"
        self.hoogteBuitenzijde.definition = "De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."
        self.hoogteBuitenzijde.constraints = ""
        self.hoogteBuitenzijde.usagenote = ""
        self.hoogteBuitenzijde.deprecated_version = ""

        self.isManToegankelijk = BooleanField(naam="isManToegankelijk",
                                              label="is man toegankelijk",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isManToegankelijk",
                                              definition="Bepaalt of de buis toegankelijk is voor een persoon.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """Bepaalt of de buis toegankelijk is voor een persoon."""

        self.isOpgevuld = BooleanField(naam="isOpgevuld",
                                       label="is opgevuld",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isOpgevuld",
                                       definition="Geeft aan of de buis gestabiliseerd/opgevuld is of niet.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Geeft aan of de buis gestabiliseerd/opgevuld is of niet."""

        self.lengte = KwantWrdInMeter()
        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte"
        self.lengte.definition = "De totale lengte in meter van de buis tussen opwaartse en afwaartse put."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de buis."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = "Bestanden van het type xlsx of pdf."
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de buis."""

        self.toestandBuis = DteTekstblok()
        """Opmerkingen van de toestand en staat van de buis."""
        self.toestandBuis.naam = "toestandBuis"
        self.toestandBuis.label = "toestand buis"
        self.toestandBuis.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis"
        self.toestandBuis.definition = "Opmerkingen van de toestand en staat van de buis."
        self.toestandBuis.constraints = ""
        self.toestandBuis.usagenote = ""
        self.toestandBuis.deprecated_version = ""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlRioleringVorm(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.vorm",
                                    definition="Bepaalt de vorm van de buis.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaalt de vorm van de buis."""
