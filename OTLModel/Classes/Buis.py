# coding=utf-8
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

        self.waarde.bokAfwaarts = KwantWrdInMeterTAW()
        """Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."""
        self.waarde.bokAfwaarts.naam = "bokAfwaarts"
        self.waarde.bokAfwaarts.label = "bok afwaarts"
        self.waarde.bokAfwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokAfwaarts"
        self.waarde.bokAfwaarts.definition = "Peil in meter-TAW van de vloei aan de afwaartse kant van de buis."
        self.waarde.bokAfwaarts.constraints = ""
        self.waarde.bokAfwaarts.usagenote = ""
        self.waarde.bokAfwaarts.deprecated_version = ""
        self.bokAfwaarts = self.waarde.bokAfwaarts

        self.waarde.bokOpwaarts = KwantWrdInMeterTAW()
        """Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."""
        self.waarde.bokOpwaarts.naam = "bokOpwaarts"
        self.waarde.bokOpwaarts.label = "bok opwaarts"
        self.waarde.bokOpwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.bokOpwaarts"
        self.waarde.bokOpwaarts.definition = "Peil in meter-TAW van de vloei aan de opwaartse kant van de buis."
        self.waarde.bokOpwaarts.constraints = ""
        self.waarde.bokOpwaarts.usagenote = ""
        self.waarde.bokOpwaarts.deprecated_version = ""
        self.bokOpwaarts = self.waarde.bokOpwaarts

        self.waarde.breedteBinnenzijde = KwantWrdInMillimeter()
        """De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        self.waarde.breedteBinnenzijde.naam = "breedteBinnenzijde"
        self.waarde.breedteBinnenzijde.label = "breedte binnenzijde"
        self.waarde.breedteBinnenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBinnenzijde"
        self.waarde.breedteBinnenzijde.definition = "De breedte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."
        self.waarde.breedteBinnenzijde.constraints = ""
        self.waarde.breedteBinnenzijde.usagenote = ""
        self.waarde.breedteBinnenzijde.deprecated_version = ""
        self.breedteBinnenzijde = self.waarde.breedteBinnenzijde

        self.waarde.breedteBuitenzijde = KwantWrdInMillimeter()
        """De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        self.waarde.breedteBuitenzijde.naam = "breedteBuitenzijde"
        self.waarde.breedteBuitenzijde.label = "breedte buitenzijde"
        self.waarde.breedteBuitenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.breedteBuitenzijde"
        self.waarde.breedteBuitenzijde.definition = "De breedte van de buitenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."
        self.waarde.breedteBuitenzijde.constraints = ""
        self.waarde.breedteBuitenzijde.usagenote = ""
        self.waarde.breedteBuitenzijde.deprecated_version = ""
        self.breedteBuitenzijde = self.waarde.breedteBuitenzijde

        self.waarde.diepteAfwaarts = KwantWrdInMeter()
        """Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        self.waarde.diepteAfwaarts.naam = "diepteAfwaarts"
        self.waarde.diepteAfwaarts.label = "diepte afwaarts"
        self.waarde.diepteAfwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteAfwaarts"
        self.waarde.diepteAfwaarts.definition = "Diepte van de vloei aan de afwaartse kant van de buis t.o.v. de bovenkant van het deksel."
        self.waarde.diepteAfwaarts.constraints = ""
        self.waarde.diepteAfwaarts.usagenote = ""
        self.waarde.diepteAfwaarts.deprecated_version = ""
        self.diepteAfwaarts = self.waarde.diepteAfwaarts

        self.waarde.diepteOpwaarts = KwantWrdInMeter()
        """De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."""
        self.waarde.diepteOpwaarts.naam = "diepteOpwaarts"
        self.waarde.diepteOpwaarts.label = "diepte opwaarts"
        self.waarde.diepteOpwaarts.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.diepteOpwaarts"
        self.waarde.diepteOpwaarts.definition = "De diepte van de vloei aan de opwaartse kant van de buis t.o.v. de bovenkant van het deksel."
        self.waarde.diepteOpwaarts.constraints = ""
        self.waarde.diepteOpwaarts.usagenote = ""
        self.waarde.diepteOpwaarts.deprecated_version = ""
        self.diepteOpwaarts = self.waarde.diepteOpwaarts

        self.waarde.helling = KwantWrdInPromille()
        """De helling van de buis in de lengterichting, uitgedrukt in promille."""
        self.waarde.helling.naam = "helling"
        self.waarde.helling.label = "helling"
        self.waarde.helling.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.helling"
        self.waarde.helling.definition = "De helling van de buis in de lengterichting, uitgedrukt in promille."
        self.waarde.helling.constraints = ""
        self.waarde.helling.usagenote = ""
        self.waarde.helling.deprecated_version = ""
        self.helling = self.waarde.helling

        self.waarde.hoogteBinnenzijde = KwantWrdInMillimeter()
        """De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."""
        self.waarde.hoogteBinnenzijde.naam = "hoogteBinnenzijde"
        self.waarde.hoogteBinnenzijde.label = "hoogte binnenzijde"
        self.waarde.hoogteBinnenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBinnenzijde"
        self.waarde.hoogteBinnenzijde.definition = "De hoogte van de binnenzijde van de buis in millimeter. Bij cirkelvormige buizen is dit de binnendiameter."
        self.waarde.hoogteBinnenzijde.constraints = ""
        self.waarde.hoogteBinnenzijde.usagenote = ""
        self.waarde.hoogteBinnenzijde.deprecated_version = ""
        self.hoogteBinnenzijde = self.waarde.hoogteBinnenzijde

        self.waarde.hoogteBuitenzijde = KwantWrdInMillimeter()
        """De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."""
        self.waarde.hoogteBuitenzijde.naam = "hoogteBuitenzijde"
        self.waarde.hoogteBuitenzijde.label = "hoogte buitenzijde"
        self.waarde.hoogteBuitenzijde.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.hoogteBuitenzijde"
        self.waarde.hoogteBuitenzijde.definition = "De hoogte van de buitenzijde van een buis in millimeter. Bij cirkelvormige buizen is dit de buitendiameter."
        self.waarde.hoogteBuitenzijde.constraints = ""
        self.waarde.hoogteBuitenzijde.usagenote = ""
        self.waarde.hoogteBuitenzijde.deprecated_version = ""
        self.hoogteBuitenzijde = self.waarde.hoogteBuitenzijde

        self.waarde.isManToegankelijk = BooleanField(naam="isManToegankelijk",
                                                     label="is man toegankelijk",
                                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isManToegankelijk",
                                                     definition="Bepaalt of de buis toegankelijk is voor een persoon.",
                                                     constraints="",
                                                     usagenote="",
                                                     deprecated_version="")
        self.isManToegankelijk = self.waarde.isManToegankelijk
        """Bepaalt of de buis toegankelijk is voor een persoon."""

        self.waarde.isOpgevuld = BooleanField(naam="isOpgevuld",
                                              label="is opgevuld",
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.isOpgevuld",
                                              definition="Geeft aan of de buis gestabiliseerd/opgevuld is of niet.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        self.isOpgevuld = self.waarde.isOpgevuld
        """Geeft aan of de buis gestabiliseerd/opgevuld is of niet."""

        self.waarde.lengte = KwantWrdInMeter()
        """De totale lengte in meter van de buis tussen opwaartse en afwaartse put."""
        self.waarde.lengte.naam = "lengte"
        self.waarde.lengte.label = "lengte"
        self.waarde.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.lengte"
        self.waarde.lengte.definition = "De totale lengte in meter van de buis tussen opwaartse en afwaartse put."
        self.waarde.lengte.constraints = ""
        self.waarde.lengte.usagenote = ""
        self.waarde.lengte.deprecated_version = ""
        self.lengte = self.waarde.lengte

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de buis."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = "Bestanden van het type xlsx of pdf."
        technischeFicheField.deprecated_version = ""
        self.waarde.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        self.technischeFiche = self.waarde.technischeFiche
        """De technische fiche van de buis."""

        self.waarde.toestandBuis = DteTekstblok()
        """Opmerkingen van de toestand en staat van de buis."""
        self.waarde.toestandBuis.naam = "toestandBuis"
        self.waarde.toestandBuis.label = "toestand buis"
        self.waarde.toestandBuis.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.toestandBuis"
        self.waarde.toestandBuis.definition = "Opmerkingen van de toestand en staat van de buis."
        self.waarde.toestandBuis.constraints = ""
        self.waarde.toestandBuis.usagenote = ""
        self.waarde.toestandBuis.deprecated_version = ""
        self.toestandBuis = self.waarde.toestandBuis

        self.waarde.vorm = KeuzelijstField(naam="vorm",
                                           label="vorm",
                                           lijst=KlRioleringVorm(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis.vorm",
                                           definition="Bepaalt de vorm van de buis.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.vorm = self.waarde.vorm
        """Bepaalt de vorm van de buis."""
