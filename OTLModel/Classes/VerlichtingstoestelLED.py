from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
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

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VerlichtingstoestelConnector.__init__(self)
        Verlichtingstoestel.__init__(self)

        self.aantalTeVerlichtenRijstroken = KeuzelijstField(naam="aantalTeVerlichtenRijstroken",
                                                            label="aantal te verlichten rijstroken",
                                                            lijst=KlWvLedAantalTeVerlichtenRijstroken(),
                                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.aantalTeVerlichtenRijstroken",
                                                            definition="Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        """Het aantal rijstroken dat verlicht wordt door het LED verlichtingstoestel."""

        self.armatuurkleur = DteKleurRAL()
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        self.armatuurkleur.naam = "armatuurkleur"
        self.armatuurkleur.label = "armatuurkleur"
        self.armatuurkleur.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.armatuurkleur"
        self.armatuurkleur.definition = "De kleur van de zichtbare buitenkant van het verlichtingstoestel."
        self.armatuurkleur.constraints = ""
        self.armatuurkleur.usagenote = ""
        self.armatuurkleur.deprecated_version = ""

        self.heeftAntiVandalisme = BooleanField(naam="heeftAntiVandalisme",
                                                label="heeft anti vandalisme",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.heeftAntiVandalisme",
                                                definition="Is het een antivandalisme type verlichtingstoestel?",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Is het een antivandalisme type verlichtingstoestel?"""

        self.isFaunavriendelijk = BooleanField(naam="isFaunavriendelijk",
                                               label="is faunavriendelijk",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.isFaunavriendelijk",
                                               definition="Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Geeft aan of de lichtkleur van de verlichting is aangepast (gebruik van oranje/rode/amberkleur ipv wit licht) zodat deze als minder storend wordt ervaren door fauna zoals bijvoorbeeld vleermuizen."""

        self.kleurTemperatuur = KeuzelijstField(naam="kleurTemperatuur",
                                                label="kleur temperatuur",
                                                lijst=KlWvLedKleurTemp(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.kleurTemperatuur",
                                                definition="Kleurtemperatuur van de LED's.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Kleurtemperatuur van de LED's."""

        self.lichtkleur = KeuzelijstField(naam="lichtkleur",
                                          label="lichtkleur",
                                          lijst=KlWvLedLichtkleur(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtkleur",
                                          definition="Beschrijving van de kleur van het licht adhv de naam van de kleur.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Beschrijving van de kleur van het licht adhv de naam van de kleur."""

        self.lichtpuntHoogte = KeuzelijstField(naam="lichtpuntHoogte",
                                               label="lichtpunt hoogte",
                                               lijst=KlWvLedLichtpunthoogte(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.lichtpuntHoogte",
                                               definition="Hoogte van het lichtpunt ten opzichte van de rijweg.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Hoogte van het lichtpunt ten opzichte van de rijweg."""

        self.overhang = KeuzelijstField(naam="overhang",
                                        label="overhang",
                                        lijst=KlWvLedOverhang(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.overhang",
                                        definition="Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Afstand tot de rand van de rijbaan van de verticale projectie van het verlichtingstoestel op de rijbaan in meter. Als de afstand tot de rijbaan gelijk is aan 0, dan valt de verticale projectie samen met de rand van de rijbaan, bij negatieve waardes ligt de verticale projectie in de berm en bij positieve waardes ligt de verticale projectie op de rijbaan"""

        self.protector = KeuzelijstField(naam="protector",
                                         label="protector",
                                         lijst=KlWvLedProtector(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.protector",
                                         definition="Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...).",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Type doorschijnende kap ter bescherming van de LED's (vlak glas, polycarbonaat,...)."""

        self.tussenAfstand = KeuzelijstField(naam="tussenAfstand",
                                             label="tussen afstand",
                                             lijst=KlWvLedTussenafstand(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.tussenAfstand",
                                             definition="Afstand tussen de verschillende LED verlichtingstoestellen.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Afstand tussen de verschillende LED verlichtingstoestellen."""

        self.verlichtingsNiveau = KeuzelijstField(naam="verlichtingsNiveau",
                                                  label="verlichtings niveau",
                                                  lijst=KlWvLedVerlNiveau(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelLED.verlichtingsNiveau",
                                                  definition="Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformeiten.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Een set van verlichtingstechnische eisen zoals gemiddelde luminantie, verlichtingssterkte, uniformeiten."""
