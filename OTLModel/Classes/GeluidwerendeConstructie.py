# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeluidwerendeConstructie(AIMObject):
    """Een geluidswerende wandvormige constructie bestaande uit een desgevallend geluidsisolerend materiaal en/of geluidsabsorberend materiaal en voorzien van de nodige structuren om de bouwkundige stabiliteit te verzekeren."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.detailplanHoogteverloop = DtcDocument()
        """Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering."""
        self.detailplanHoogteverloop.naam = "detailplanHoogteverloop"
        self.detailplanHoogteverloop.label = "detailplan hoogteverloop"
        self.detailplanHoogteverloop.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.detailplanHoogteverloop"
        self.detailplanHoogteverloop.definition = "Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering."
        self.detailplanHoogteverloop.constraints = ""
        self.detailplanHoogteverloop.usagenote = "Bestanden moeten van het type DWG of DXF zijn."
        self.detailplanHoogteverloop.deprecated_version = ""

        self.horizontaalRuimtebeslag = DtcDocument()
        """Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt."""
        self.horizontaalRuimtebeslag.naam = "horizontaalRuimtebeslag"
        self.horizontaalRuimtebeslag.label = "horizontaal ruimtebeslag"
        self.horizontaalRuimtebeslag.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.horizontaalRuimtebeslag"
        self.horizontaalRuimtebeslag.definition = "Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt."
        self.horizontaalRuimtebeslag.constraints = ""
        self.horizontaalRuimtebeslag.usagenote = ""
        self.horizontaalRuimtebeslag.deprecated_version = ""

        overzichtsafbeeldingField = DtcDocument()
        overzichtsafbeeldingField.naam = "overzichtsafbeelding"
        overzichtsafbeeldingField.label = "overzichtsafbeelding"
        overzichtsafbeeldingField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.overzichtsafbeelding"
        overzichtsafbeeldingField.definition = "Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie."
        overzichtsafbeeldingField.constraints = ""
        overzichtsafbeeldingField.usagenote = ""
        overzichtsafbeeldingField.deprecated_version = ""
        self.overzichtsafbeelding = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=overzichtsafbeeldingField)
        """Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie."""

        rekennotaField = DtcDocument()
        rekennotaField.naam = "rekennota"
        rekennotaField.label = "rekennota"
        rekennotaField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.rekennota"
        rekennotaField.definition = "Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie)."
        rekennotaField.constraints = ""
        rekennotaField.usagenote = ""
        rekennotaField.deprecated_version = ""
        self.rekennota = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=rekennotaField)
        """Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie)."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.technischeFiche"
        technischeFicheField.definition = "Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken."""

        self.totaleLengte = KwantWrdInMeter()
        """De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie."""
        self.totaleLengte.naam = "totaleLengte"
        self.totaleLengte.label = "totale lengte"
        self.totaleLengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleLengte"
        self.totaleLengte.definition = "De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie."
        self.totaleLengte.constraints = ""
        self.totaleLengte.usagenote = ""
        self.totaleLengte.deprecated_version = ""

        self.totaleOppervlakte = KwantWrdInVierkanteMeter()
        """De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie."""
        self.totaleOppervlakte.naam = "totaleOppervlakte"
        self.totaleOppervlakte.label = "totale oppervlakte"
        self.totaleOppervlakte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleOppervlakte"
        self.totaleOppervlakte.definition = "De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie."
        self.totaleOppervlakte.constraints = ""
        self.totaleOppervlakte.usagenote = ""
        self.totaleOppervlakte.deprecated_version = ""
