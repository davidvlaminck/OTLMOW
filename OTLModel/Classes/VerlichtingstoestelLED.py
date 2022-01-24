# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.KlWvLedAantalTeVerlichtenRijstroken import KlWvLedAantalTeVerlichtenRijstroken
from OTLModel.Datatypes.KlWvLedKleurTemp import KlWvLedKleurTemp
from OTLModel.Datatypes.KlWvLedLichtkleur import KlWvLedLichtkleur
from OTLModel.Datatypes.KlWvLedLichtpunthoogte import KlWvLedLichtpunthoogte
from OTLModel.Datatypes.KlWvLedOverhang import KlWvLedOverhang
from OTLModel.Datatypes.KlWvLedProtector import KlWvLedProtector
from OTLModel.Datatypes.KlWvLedTussenafstand import KlWvLedTussenafstand
from OTLModel.Datatypes.KlWvLedVerlNiveau import KlWvLedVerlNiveau


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelLED(VerlichtingstoestelConnector, Verlichtingstoestel):
    """Het geheel van de LEDlichtmodule en de behuizing die werden samengesteld met als doel:
 * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
 * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
 * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen
De LED driver bevindt zich fysiek in het verlichtingstoestel maar wordt als een appart onderdeel behandeld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)

        self._aantalTeVerlichtenRijstroken = OTLAttribuut(field=KlWvLedAantalTeVerlichtenRijstroken,
                                                          naam='aantalTeVerlichtenRijstroken',
                                                          label='aantal te verlichten rijstroken',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.aantalTeVerlichtenRijstroken',
                                                          definition='Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.')

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.armatuurkleur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.')

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?')

        self._isFaunavriendelijk = OTLAttribuut(field=BooleanField,
                                                naam='isFaunavriendelijk',
                                                label='is faunavriendelijk',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isFaunavriendelijk',
                                                definition='Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen.')

        self._kleurTemperatuur = OTLAttribuut(field=KlWvLedKleurTemp,
                                              naam='kleurTemperatuur',
                                              label='kleur temperatuur',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurTemperatuur',
                                              definition="Kleurtemperatuur van de LED's.")

        self._lichtkleur = OTLAttribuut(field=KlWvLedLichtkleur,
                                        naam='lichtkleur',
                                        label='lichtkleur',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtkleur',
                                        definition='Beschrijving van de kleur van het licht adhv de naam van de kleur.')

        self._lichtpuntHoogte = OTLAttribuut(field=KlWvLedLichtpunthoogte,
                                             naam='lichtpuntHoogte',
                                             label='lichtpunt hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtpuntHoogte',
                                             definition='Hoogte van het lichtpunt ten opzichte van de rijweg.')

        self._overhang = OTLAttribuut(field=KlWvLedOverhang,
                                      naam='overhang',
                                      label='overhang',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.overhang',
                                      definition='Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan')

        self._protector = OTLAttribuut(field=KlWvLedProtector,
                                       naam='protector',
                                       label='protector',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.protector',
                                       definition="Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...).")

        self._tussenAfstand = OTLAttribuut(field=KlWvLedTussenafstand,
                                           naam='tussenAfstand',
                                           label='tussen afstand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.tussenAfstand',
                                           definition='Afstand tussen de verschillende LED verlichtingstoestellen.')

        self._verlichtingsNiveau = OTLAttribuut(field=KlWvLedVerlNiveau,
                                                naam='verlichtingsNiveau',
                                                label='verlichtings niveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.verlichtingsNiveau',
                                                definition='Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformeiten.')

    @property
    def aantalTeVerlichtenRijstroken(self):
        """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""
        return self._aantalTeVerlichtenRijstroken.waarde

    @aantalTeVerlichtenRijstroken.setter
    def aantalTeVerlichtenRijstroken(self, value):
        self._aantalTeVerlichtenRijstroken.set_waarde(value, owner=self)

    @property
    def armatuurkleur(self):
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        return self._armatuurkleur.waarde

    @armatuurkleur.setter
    def armatuurkleur(self, value):
        self._armatuurkleur.set_waarde(value, owner=self)

    @property
    def heeftAntiVandalisme(self):
        """Is het een antivandalisme type verlichtingstoestel?"""
        return self._heeftAntiVandalisme.waarde

    @heeftAntiVandalisme.setter
    def heeftAntiVandalisme(self, value):
        self._heeftAntiVandalisme.set_waarde(value, owner=self)

    @property
    def isFaunavriendelijk(self):
        """Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen."""
        return self._isFaunavriendelijk.waarde

    @isFaunavriendelijk.setter
    def isFaunavriendelijk(self, value):
        self._isFaunavriendelijk.set_waarde(value, owner=self)

    @property
    def kleurTemperatuur(self):
        """Kleurtemperatuur van de LED's."""
        return self._kleurTemperatuur.waarde

    @kleurTemperatuur.setter
    def kleurTemperatuur(self, value):
        self._kleurTemperatuur.set_waarde(value, owner=self)

    @property
    def lichtkleur(self):
        """Beschrijving van de kleur van het licht adhv de naam van de kleur."""
        return self._lichtkleur.waarde

    @lichtkleur.setter
    def lichtkleur(self, value):
        self._lichtkleur.set_waarde(value, owner=self)

    @property
    def lichtpuntHoogte(self):
        """Hoogte van het lichtpunt ten opzichte van de rijweg."""
        return self._lichtpuntHoogte.waarde

    @lichtpuntHoogte.setter
    def lichtpuntHoogte(self, value):
        self._lichtpuntHoogte.set_waarde(value, owner=self)

    @property
    def overhang(self):
        """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan"""
        return self._overhang.waarde

    @overhang.setter
    def overhang(self, value):
        self._overhang.set_waarde(value, owner=self)

    @property
    def protector(self):
        """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""
        return self._protector.waarde

    @protector.setter
    def protector(self, value):
        self._protector.set_waarde(value, owner=self)

    @property
    def tussenAfstand(self):
        """Afstand tussen de verschillende LED verlichtingstoestellen."""
        return self._tussenAfstand.waarde

    @tussenAfstand.setter
    def tussenAfstand(self, value):
        self._tussenAfstand.set_waarde(value, owner=self)

    @property
    def verlichtingsNiveau(self):
        """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformeiten."""
        return self._verlichtingsNiveau.waarde

    @verlichtingsNiveau.setter
    def verlichtingsNiveau(self, value):
        self._verlichtingsNiveau.set_waarde(value, owner=self)
