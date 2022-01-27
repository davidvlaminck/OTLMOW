# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.VRIDraagconstructie import VRIDraagconstructie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KlSeinbrugRijrichting import KlSeinbrugRijrichting
from OTLMOW.OTLModel.Datatypes.KlSeinbrugType import KlSeinbrugType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Seinbrug(VRIDraagconstructie):
    """Metalen constructie bestaande uit twee of meer verticale steunen met voetplaat en uit een enkele of een dubbel uitgevoerde horizontale dwarsverbinding, allen kokervormig met rechthoekige doorsnede. Ook wel portiek of portaal genoemd."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalLadders = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalLadders',
                                           label='aantal ladders',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalLadders',
                                           definition='Het aantal ladders waarmee de seinbrug toegankelijk is.')

        self._aantalSteunen = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalSteunen',
                                           label='aantal steunen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.aantalSteunen',
                                           definition='Het aantal steunen waarmee de seinbrug gedragen wordt. ')

        self._berekeningsnota = OTLAttribuut(field=DtcDocument,
                                             naam='berekeningsnota',
                                             label='berekeningsnota',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.berekeningsnota',
                                             definition='Een bijlage met de berekeningsnota voor de seinbrug.')

        self._controlemetingEBS = OTLAttribuut(field=DtcDocument,
                                               naam='controlemetingEBS',
                                               label='controlemeting EBS',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.controlemetingEBS',
                                               definition='Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal.')

        self._heeftLooproosters = OTLAttribuut(field=BooleanField,
                                               naam='heeftLooproosters',
                                               label='heeft looproosters',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.heeftLooproosters',
                                               definition='Geeft aan of de seinbrug is uitgerust met looproosters.')

        self._hoogteVerticaleSteun = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='hoogteVerticaleSteun',
                                                  label='hoogte verticale steun',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.hoogteVerticaleSteun',
                                                  definition='Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug.')

        self._overspanning = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='overspanning',
                                          label='overspanning',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.overspanning',
                                          definition='De afstand tussen de twee steunpunten van de seinbrug.')

        self._rijrichting = OTLAttribuut(field=KlSeinbrugRijrichting,
                                         naam='rijrichting',
                                         label='rijrichting',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.rijrichting',
                                         definition='Geeft aan of de seinbrug één of beide rijrichtingen overspant.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.technischeFiche',
                                             definition='Een bijlage waarin de detailtekeningen van de seinbrug.')

        self._type = OTLAttribuut(field=KlSeinbrugType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.type',
                                  definition='Het type van de seinbrug volgens de aard van de constructie.')

        self._vrijeHoogte = OTLAttribuut(field=KwantWrdInMeter,
                                         naam='vrijeHoogte',
                                         label='vrije hoogte',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Seinbrug.vrijeHoogte',
                                         definition='De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug.')

    @property
    def aantalLadders(self):
        """Het aantal ladders waarmee de seinbrug toegankelijk is."""
        return self._aantalLadders.waarde

    @aantalLadders.setter
    def aantalLadders(self, value):
        self._aantalLadders.set_waarde(value, owner=self)

    @property
    def aantalSteunen(self):
        """Het aantal steunen waarmee de seinbrug gedragen wordt. """
        return self._aantalSteunen.waarde

    @aantalSteunen.setter
    def aantalSteunen(self, value):
        self._aantalSteunen.set_waarde(value, owner=self)

    @property
    def berekeningsnota(self):
        """Een bijlage met de berekeningsnota voor de seinbrug."""
        return self._berekeningsnota.waarde

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def controlemetingEBS(self):
        """Een bijlage met het verslag van de controlemeting uitgevoerd door het Expertisecentrum Beton en Staal."""
        return self._controlemetingEBS.waarde

    @controlemetingEBS.setter
    def controlemetingEBS(self, value):
        self._controlemetingEBS.set_waarde(value, owner=self)

    @property
    def heeftLooproosters(self):
        """Geeft aan of de seinbrug is uitgerust met looproosters."""
        return self._heeftLooproosters.waarde

    @heeftLooproosters.setter
    def heeftLooproosters(self, value):
        self._heeftLooproosters.set_waarde(value, owner=self)

    @property
    def hoogteVerticaleSteun(self):
        """Verticale afstand (in meter) tussen de bovenkant van het wegdek en de bovenkant van het hoogste constructiedeel van de seinbrug."""
        return self._hoogteVerticaleSteun.waarde

    @hoogteVerticaleSteun.setter
    def hoogteVerticaleSteun(self, value):
        self._hoogteVerticaleSteun.set_waarde(value, owner=self)

    @property
    def overspanning(self):
        """De afstand tussen de twee steunpunten van de seinbrug."""
        return self._overspanning.waarde

    @overspanning.setter
    def overspanning(self, value):
        self._overspanning.set_waarde(value, owner=self)

    @property
    def rijrichting(self):
        """Geeft aan of de seinbrug één of beide rijrichtingen overspant."""
        return self._rijrichting.waarde

    @rijrichting.setter
    def rijrichting(self, value):
        self._rijrichting.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Een bijlage waarin de detailtekeningen van de seinbrug."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de seinbrug volgens de aard van de constructie."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def vrijeHoogte(self):
        """De verticale afstand (in meter) tussen de bovenkant van het wegdek en de onderkant van het laagste, daarboven gelegen constructiedeel van de seinbrug."""
        return self._vrijeHoogte.waarde

    @vrijeHoogte.setter
    def vrijeHoogte(self, value):
        self._vrijeHoogte.set_waarde(value, owner=self)
