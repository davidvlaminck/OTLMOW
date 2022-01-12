# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieType(Keuzelijst):
    """Types van figuratiemarkering."""

    def __init__(self):
        super().__init__(naam="KlFiguratieType",
                         label="Figuratie type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieType",
                         definition="Types van figuratiemarkering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieType")

        self.add_option("2e-afslag-links-(5m)", "2e afslag links (5m)", "Pijl 2e afslag links (5m).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-links-(5m)")
        self.add_option("2e-afslag-links-(7.5m)", "2e afslag links (7.5m)", "Pijl 2e afslag links (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-links-(7.5m)")
        self.add_option("2e-afslag-rechts-(5m)", "2e afslag rechts (5m)", "Pijl 2e afslag rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-rechts-(5m)")
        self.add_option("2e-afslag-rechts-(7.5m)", "2e afslag rechts (7.5m)", "Pijl 2e afslag rechts (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/2e-afslag-rechts-(7.5m)")
        self.add_option("BUS-(dwars-op-BOB)", "BUS (dwars op BOB)", "Lettermarkering van bus (dwars op BOB)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(dwars-op-BOB)")
        self.add_option("BUS-(dwars-op-busstrook)", "BUS (dwars op busstrook)", "Lettermarkering van bus (dwars op busstrook)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(dwars-op-busstrook)")
        self.add_option("BUS-(langs-op-BOB)", "BUS (langs op BOB)", "Lettermarkering van bus (langs op BOB)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/BUS-(langs-op-BOB)")
        self.add_option("STOP", "STOP", "Lettermarkering STOP", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/STOP")
        self.add_option("STOP-(smal)", "STOP (smal)", "Lettermarkering STOP (smal)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/STOP-(smal)")
        self.add_option("TAXI-(dwars)", "TAXI (dwars)", "Lettermarkering van taxiplaats (dwars)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TAXI-(dwars)")
        self.add_option("TAXI-(langs)", "TAXI (langs)", "Lettermarkering van taxiplaats (langs)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TAXI-(langs)")
        self.add_option("TRAM-(dwars)", "TRAM (dwars)", "Lettermarkering van tramhalte (dwars)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TRAM-(dwars)")
        self.add_option("TRAM-(langs)", "TRAM (langs)", "Lettermarkering van tramhalte (langs)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/TRAM-(langs)")
        self.add_option("autocar", "autocar", "Symbool autocar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/autocar")
        self.add_option("blauwe-zone-(parkeerschijf)", "blauwe zone (parkeerschijf)", "Verkeersbordmarkering blauwe zone (parkeerschijf).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/blauwe-zone-(parkeerschijf)")
        self.add_option("bromfiets-groot", "bromfiets groot", "Symbool bromfiets groot.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bromfiets-groot")
        self.add_option("bromfiets-klein", "bromfiets klein", "Symbool bromfiets klein.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bromfiets-klein")
        self.add_option("bushalte-op-de-rijweg", "bushalte op de rijweg", "Lettermarkering bus zonder arcering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/bushalte-op-de-rijweg")
        self.add_option("elektrische-voertuigen-normaal", "elektrische voertuigen normaal", "Symbool elektrische voertuigen normaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-normaal")
        self.add_option("elektrische-voertuigen-vergroot", "elektrische voertuigen vergroot", "Symbool elektrische voertuigen vergroot.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-vergroot")
        self.add_option("elektrische-voertuigen-verkleind", "elektrische voertuigen verkleind", "Symbool elektrische voertuigen verkleind.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/elektrische-voertuigen-verkleind")
        self.add_option("fietslogo-Groot", "fietslogo Groot", "Logomarkering fiestslogo Groot.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietslogo-Groot")
        self.add_option("fietslogo-Klein", "fietslogo Klein", "Logomarkering fiestslogo Klein.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietslogo-Klein")
        self.add_option("fietspadpijl-(klein---dubbele-fietspadpijl)", "fietspadpijl (klein - dubbele fietspadpijl)", "Pijl Fietspadpijl (klein - dubbele fietspadpijl)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietspadpijl-(klein---dubbele-fietspadpijl)")
        self.add_option("fietspadpijl-(std)", "fietspadpijl (std)", "Pijl Fietspadpijl (std)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietspadpijl-(std)")
        self.add_option("fietsstraat-begin", "fietsstraat begin", "Verkeersbord F111 dat het einde van de fietsstraat aanduidt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsstraat-begin")
        self.add_option("fietsstraat-einde", "fietsstraat einde", "Verkeersbord F113 dat het einde van de fietsstraat aanduidt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsstraat-einde")
        self.add_option("fietsvoorsortering-Links", "fietsvoorsortering Links", "Pijl Fietsvoorsortering Links", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/fietsvoorsortering-Links")
        self.add_option("groot", "groot", "Omgekeerde driehoek markering groot type.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/groot")
        self.add_option("groter-dan-22.75-m²", "groter dan 22.75 m²", "Lettermarkering bus met arcering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/groter-dan-22.75-m²")
        self.add_option("klein", "klein", "Omgekeerde driehoek markering klein type.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/klein")
        self.add_option("kleiner-dan-22.75-m²", "kleiner dan 22.75 m²", "Lettermarkering bus met arcering.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/kleiner-dan-22.75-m²")
        self.add_option("kruising-sporen", "kruising sporen", "Aanduiding A49 kruising van een openbare weg door één of meer in de rijbaan aangelegde sporen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/kruising-sporen")
        self.add_option("links-(5m)", "links (5m)", "Pijl Links (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-(5m)")
        self.add_option("links-(7.5m)", "links (7.5m)", "Pijl Links (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-(7.5m)")
        self.add_option("links-+-Rechts-(5m)", "links + Rechts (5m)", "Pijl Links + Rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-+-Rechts-(5m)")
        self.add_option("links-+-Rechts-(7.5m)", "links + Rechts (7.5m)", "Pijl Links + Rechts (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/links-+-Rechts-(7.5m)")
        self.add_option("mindervaliden-logo-klein", "mindervaliden logo klein", "Logomarkering Mindervaliden klein.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-klein")
        self.add_option("mindervaliden-logo-normaal", "mindervaliden logo normaal", "Logomarkering Mindervaliden normaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-normaal")
        self.add_option("mindervaliden-logo-vergroot", "mindervaliden logo vergroot", "Logomarkering Mindervaliden vergroot.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/mindervaliden-logo-vergroot")
        self.add_option("null", "null", "Geen aanduiding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/null")
        self.add_option("oversteekplaats-voor-voetgangers", "oversteekplaats voor voetgangers", "Aanduiding A21 oversteekplaats voor voetgangers.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/oversteekplaats-voor-voetgangers")
        self.add_option("parkeerverbod", "parkeerverbod", "Verkeersbordmarkering parkeerverbod.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/parkeerverbod")
        self.add_option("rechtdoor-(5m)", "rechtdoor (5m)", "Pijl rechtdoor (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-(5m)")
        self.add_option("rechtdoor-+-Links-(5m)", "rechtdoor + Links (5m)", "Pijl Rechtdoor + Links (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-(5m)")
        self.add_option("rechtdoor-+-Links-(7.5m)", "rechtdoor + Links (7.5m)", "Pijl Rechtdoor + Links (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-(7.5m)")
        self.add_option("rechtdoor-+-Links-+-Rechts-(5m)", "rechtdoor + Links + Rechts (5m)", "Pijl Rechtdoor + Links + Rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-+-Rechts-(5m)")
        self.add_option("rechtdoor-+-Links-+-Rechts-(7.5m)", "rechtdoor + Links + Rechts (7.5m)", "Pijl Rechtdoor + Links + Rechts (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Links-+-Rechts-(7.5m)")
        self.add_option("rechtdoor-+-Rechts-(5m)", "rechtdoor + Rechts (5m)", "Pijl Rechtdoor + Rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Rechts-(5m)")
        self.add_option("rechtdoor-+-Rechts-(7.5m)", "rechtdoor + Rechts (7.5m)", "Pijl Rechtdoor + Rechts (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechtdoor-+-Rechts-(7.5m)")
        self.add_option("rechts-(5m)", "rechts (5m)", "Pijl Rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechts-(5m)")
        self.add_option("rechts-(7.5m)", "rechts (7.5m)", "Pijl Rechts (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rechts-(7.5m)")
        self.add_option("rijstrook-vermindering-links", "rijstrook vermindering links", "Pijl Rijstrook vermindering links", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rijstrook-vermindering-links")
        self.add_option("rijstrook-vermindering-rechts", "rijstrook vermindering rechts", "Pijl Rijstrook vermindering rechts", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/rijstrook-vermindering-rechts")
        self.add_option("schoolkinderen", "schoolkinderen", "Verkeersbordmarkering schoolkinderen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/schoolkinderen")
        self.add_option("turborotonde-Links", "turborotonde Links", "Pijl Turborotonde Links", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Links")
        self.add_option("turborotonde-Rechtdoor", "turborotonde Rechtdoor", "Pijl Turborotonde Rechtdoor", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor")
        self.add_option("turborotonde-Rechtdoor-en-Links", "turborotonde Rechtdoor en Links", "Pijl Turborotonde Rechtdoor en Links", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor-en-Links")
        self.add_option("turborotonde-Rechtdoor-en-Rechts", "turborotonde Rechtdoor en Rechts", "Pijl Turborotonde Rechtdoor en Rechts", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor-en-Rechts")
        self.add_option("turborotonde-Rechtdoor.-Links-en-rechts", "turborotonde Rechtdoor. Links en rechts", "Pijl Turborotonde Rechtdoor, Links en rechts", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechtdoor.-Links-en-rechts")
        self.add_option("turborotonde-Rechts", "turborotonde Rechts", "Pijl Turborotonde Rechts", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/turborotonde-Rechts")
        self.add_option("voorsortering-Links-(5m)", "voorsortering Links (5m)", "Pijl Voorsortering Links (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Links-(5m)")
        self.add_option("voorsortering-Links-(7.5m)", "voorsortering Links (7.5m)", "Pijl Voorsortering Links (7,5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Links-(7.5m)")
        self.add_option("voorsortering-Rechts-(5m)", "voorsortering Rechts (5m)", "Pijl Voorsortering Rechts (5m)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Rechts-(5m)")
        self.add_option("voorsortering-Rechts-(7.5m)", "voorsortering Rechts (7.5m)", "Aanduiding A49 kruising van een openbare weg door één of meer in de rijbaan aangelegde sporen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/voorsortering-Rechts-(7.5m)")
        self.add_option("woon-werkverkeer", "woon-werkverkeer", "Symbool woon-werkverkeer.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieType/woon-werkverkeer")
