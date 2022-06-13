# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLMOW.OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLMOW.OTLModel.Datatypes.KlArmatuurkleur import KlArmatuurkleur
from OTLMOW.OTLModel.Datatypes.KlWvLedAantalTeVerlichtenRijstroken import KlWvLedAantalTeVerlichtenRijstroken
from OTLMOW.OTLModel.Datatypes.KlWvLedKleurTemp import KlWvLedKleurTemp
from OTLMOW.OTLModel.Datatypes.KlWvLedLichtkleur import KlWvLedLichtkleur
from OTLMOW.OTLModel.Datatypes.KlWvLedLichtpunthoogte import KlWvLedLichtpunthoogte
from OTLMOW.OTLModel.Datatypes.KlWvLedOverhang import KlWvLedOverhang
from OTLMOW.OTLModel.Datatypes.KlWvLedProtector import KlWvLedProtector
from OTLMOW.OTLModel.Datatypes.KlWvLedTussenafstand import KlWvLedTussenafstand
from OTLMOW.OTLModel.Datatypes.KlWvLedVerlNiveau import KlWvLedVerlNiveau
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelLED(Verlichtingstoestel, VerlichtingstoestelConnector):
    """Het geheel van de LEDlichtmodule en de behuizing die werden samengesteld met als doel:
 * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
 * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
 * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen
De LED driver bevindt zich fysiek in het verlichtingstoestel maar wordt als een apart onderdeel behandeld."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)

        self._aantalTeVerlichtenRijstroken = OTLAttribuut(field=KlWvLedAantalTeVerlichtenRijstroken,
                                                          naam='aantalTeVerlichtenRijstroken',
                                                          label='aantal te verlichten rijstroken',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.aantalTeVerlichtenRijstroken',
                                                          definition='Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.',
                                                          owner=self)

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.armatuurkleur',
                                           usagenote='Attribuut uit gebruik sinds versie 2.3.0 ',
                                           deprecated_version='2.3.0',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?',
                                                 owner=self)

        self._isFaunavriendelijk = OTLAttribuut(field=BooleanField,
                                                naam='isFaunavriendelijk',
                                                label='is faunavriendelijk',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isFaunavriendelijk',
                                                definition='Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen.',
                                                owner=self)

        self._kleurArmatuur = OTLAttribuut(field=KlArmatuurkleur,
                                           naam='kleurArmatuur',
                                           label='kleur armatuur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurArmatuur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

        self._kleurTemperatuur = OTLAttribuut(field=KlWvLedKleurTemp,
                                              naam='kleurTemperatuur',
                                              label='kleur temperatuur',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurTemperatuur',
                                              definition="Kleurtemperatuur van de LED's.",
                                              owner=self)

        self._lichtkleur = OTLAttribuut(field=KlWvLedLichtkleur,
                                        naam='lichtkleur',
                                        label='lichtkleur',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtkleur',
                                        definition='Beschrijving van de kleur van het licht adhv de naam van de kleur.',
                                        owner=self)

        self._lichtpuntHoogte = OTLAttribuut(field=KlWvLedLichtpunthoogte,
                                             naam='lichtpuntHoogte',
                                             label='lichtpunt hoogte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtpuntHoogte',
                                             definition='Hoogte van het lichtpunt ten opzichte van de rijweg.',
                                             owner=self)

        self._overhang = OTLAttribuut(field=KlWvLedOverhang,
                                      naam='overhang',
                                      label='overhang',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.overhang',
                                      definition='Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan',
                                      owner=self)

        self._protector = OTLAttribuut(field=KlWvLedProtector,
                                       naam='protector',
                                       label='protector',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.protector',
                                       definition="Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...).",
                                       owner=self)

        self._tussenAfstand = OTLAttribuut(field=KlWvLedTussenafstand,
                                           naam='tussenAfstand',
                                           label='tussen afstand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.tussenAfstand',
                                           usagenote='Attribuut uit gebruik sinds versie 2.4.0 ',
                                           deprecated_version='2.4.0',
                                           definition='Afstand tussen de verschillende LED verlichtingstoestellen.',
                                           owner=self)

        self._tussenafstandLED = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='tussenafstandLED',
                                              label='tussenafstand LED',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.tussenafstandLED',
                                              usagenote='Maximum 1 cijfer na de komma ingeven.',
                                              definition='Afstand, uitgedrukt in meter, tussen de verschillende LED verlichtingstoestellen.',
                                              owner=self)

        self._verlichtingsNiveau = OTLAttribuut(field=KlWvLedVerlNiveau,
                                                naam='verlichtingsNiveau',
                                                label='verlichtings niveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.verlichtingsNiveau',
                                                definition='Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformiteiten.',
                                                owner=self)

    @property
    def aantalTeVerlichtenRijstroken(self):
        """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""
        return self._aantalTeVerlichtenRijstroken.get_waarde()

    @aantalTeVerlichtenRijstroken.setter
    def aantalTeVerlichtenRijstroken(self, value):
        self._aantalTeVerlichtenRijstroken.set_waarde(value, owner=self)

    @property
    def armatuurkleur(self):
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        return self._armatuurkleur.get_waarde()

    @armatuurkleur.setter
    def armatuurkleur(self, value):
        self._armatuurkleur.set_waarde(value, owner=self)

    @property
    def heeftAntiVandalisme(self):
        """Is het een antivandalisme type verlichtingstoestel?"""
        return self._heeftAntiVandalisme.get_waarde()

    @heeftAntiVandalisme.setter
    def heeftAntiVandalisme(self, value):
        self._heeftAntiVandalisme.set_waarde(value, owner=self)

    @property
    def isFaunavriendelijk(self):
        """Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen."""
        return self._isFaunavriendelijk.get_waarde()

    @isFaunavriendelijk.setter
    def isFaunavriendelijk(self, value):
        self._isFaunavriendelijk.set_waarde(value, owner=self)

    @property
    def kleurArmatuur(self):
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        return self._kleurArmatuur.get_waarde()

    @kleurArmatuur.setter
    def kleurArmatuur(self, value):
        self._kleurArmatuur.set_waarde(value, owner=self)

    @property
    def kleurTemperatuur(self):
        """Kleurtemperatuur van de LED's."""
        return self._kleurTemperatuur.get_waarde()

    @kleurTemperatuur.setter
    def kleurTemperatuur(self, value):
        self._kleurTemperatuur.set_waarde(value, owner=self)

    @property
    def lichtkleur(self):
        """Beschrijving van de kleur van het licht adhv de naam van de kleur."""
        return self._lichtkleur.get_waarde()

    @lichtkleur.setter
    def lichtkleur(self, value):
        self._lichtkleur.set_waarde(value, owner=self)

    @property
    def lichtpuntHoogte(self):
        """Hoogte van het lichtpunt ten opzichte van de rijweg."""
        return self._lichtpuntHoogte.get_waarde()

    @lichtpuntHoogte.setter
    def lichtpuntHoogte(self, value):
        self._lichtpuntHoogte.set_waarde(value, owner=self)

    @property
    def overhang(self):
        """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan"""
        return self._overhang.get_waarde()

    @overhang.setter
    def overhang(self, value):
        self._overhang.set_waarde(value, owner=self)

    @property
    def protector(self):
        """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""
        return self._protector.get_waarde()

    @protector.setter
    def protector(self, value):
        self._protector.set_waarde(value, owner=self)

    @property
    def tussenAfstand(self):
        """Afstand tussen de verschillende LED verlichtingstoestellen."""
        return self._tussenAfstand.get_waarde()

    @tussenAfstand.setter
    def tussenAfstand(self, value):
        self._tussenAfstand.set_waarde(value, owner=self)

    @property
    def tussenafstandLED(self):
        """Afstand, uitgedrukt in meter, tussen de verschillende LED verlichtingstoestellen."""
        return self._tussenafstandLED.get_waarde()

    @tussenafstandLED.setter
    def tussenafstandLED(self, value):
        self._tussenafstandLED.set_waarde(value, owner=self)

    @property
    def verlichtingsNiveau(self):
        """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformiteiten."""
        return self._verlichtingsNiveau.get_waarde()

    @verlichtingsNiveau.setter
    def verlichtingsNiveau(self, value):
        self._verlichtingsNiveau.set_waarde(value, owner=self)
