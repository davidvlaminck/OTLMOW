# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class GeluidwerendeConstructie(AIMObject):
    """Een geluidswerende wandvormige constructie bestaande uit een desgevallend geluidsisolerend materiaal en/of geluidsabsorberend materiaal en voorzien van de nodige structuren om de bouwkundige stabiliteit te verzekeren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._detailplanHoogteverloop = OTLAttribuut(field=DtcDocument,
                                                     naam='detailplanHoogteverloop',
                                                     label='detailplan hoogteverloop',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.detailplanHoogteverloop',
                                                     usagenote='Bestanden moeten van het type DWG of DXF zijn.',
                                                     definition='Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering.')

        self._horizontaalRuimtebeslag = OTLAttribuut(field=DtcDocument,
                                                     naam='horizontaalRuimtebeslag',
                                                     label='horizontaal ruimtebeslag',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.horizontaalRuimtebeslag',
                                                     definition='Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt.')

        self._overzichtsafbeelding = OTLAttribuut(field=DtcDocument,
                                                  naam='overzichtsafbeelding',
                                                  label='overzichtsafbeelding',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.overzichtsafbeelding',
                                                  kardinaliteit_max='*',
                                                  definition='Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie.')

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.rekennota',
                                       kardinaliteit_max='*',
                                       definition='Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie).')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken.')

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleLengte',
                                          definition='De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie.')

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#GeluidwerendeConstructie.totaleOppervlakte',
                                               definition='De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie.')

    @property
    def detailplanHoogteverloop(self):
        """Dit is een detailplan in de vorm van een lijn waarin het verloop van de absolute hoogte van de top van de geluidswerende constructie wordt weergegeven. Minstens om de 10 meter wordt de hoogte van de top van de constructie bepaald. Het detailplan wordt gebruikt voor akoestische modellering."""
        return self._detailplanHoogteverloop.waarde

    @detailplanHoogteverloop.setter
    def detailplanHoogteverloop(self, value):
        self._detailplanHoogteverloop.set_waarde(value, owner=self)

    @property
    def horizontaalRuimtebeslag(self):
        """Document waarin de variatie in horizontaal ruimtebeslag over het verloop van de geluidswerende constructie is weergegeven. Het horizontaal ruimtebeslag is de breedte die de gehele constructie inneemt op het maaiveld, loodrecht op de richting waarin de schermelementen op elkaar aangesloten zijn. Er moet een nieuwe waarde ingegeven worden elke keer als de hoogte van de constructie wijzigt."""
        return self._horizontaalRuimtebeslag.waarde

    @horizontaalRuimtebeslag.setter
    def horizontaalRuimtebeslag(self, value):
        self._horizontaalRuimtebeslag.set_waarde(value, owner=self)

    @property
    def overzichtsafbeelding(self):
        """Dit een overzichtsfoto van de hele constructie. Op basis van deze afbeelding kan je snel bekijken hoe de kleur of hoogte varieert over het verloop van de geluidswerende constructie."""
        return self._overzichtsafbeelding.waarde

    @overzichtsafbeelding.setter
    def overzichtsafbeelding(self, value):
        self._overzichtsafbeelding.set_waarde(value, owner=self)

    @property
    def rekennota(self):
        """Dit is een document waarin allerlei berekeningen bijgehouden worden omtrent de stabiliteit en sterkte van de geluidswerende constructie (oa de variatie in statische belasting en windbelasting over het verloop van geluidswerende constructie)."""
        return self._rekennota.waarde

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Dit document geeft volgende zaken mee: producent, productnaam (type), beschrijving van de geplaatste constructie, certificatie (CE en ISO), montage, akoestische karakteristieken, duurzaamheid en brandwerende kenmerken."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def totaleLengte(self):
        """De afstand in meter gemeten tussen het beginpunt en het eindpunt van de geluidswerende constructie."""
        return self._totaleLengte.waarde

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def totaleOppervlakte(self):
        """De totale oppervlakte van het naar de weg gerichte vlak van alle geplaatste schermelementen van de geluidswerende constructie."""
        return self._totaleOppervlakte.waarde

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)
