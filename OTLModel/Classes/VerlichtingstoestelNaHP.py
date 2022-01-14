# coding=utf-8
from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelNaHP(VerlichtingstoestelConnector, Verlichtingstoestel):
    """Het geheel van de natrium hoge druk lamp (NaHP) en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)

        self.armatuurkleur = DteKleurRAL()
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        self.armatuurkleur.naam = "armatuurkleur"
        self.armatuurkleur.label = "armatuurkleur"
        self.armatuurkleur.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.armatuurkleur"
        self.armatuurkleur.definition = "De kleur van de zichtbare buitenkant van het verlichtingstoestel."
        self.armatuurkleur.constraints = ""
        self.armatuurkleur.usagenote = ""
        self.armatuurkleur.deprecated_version = ""

        self.heeftAntiVandalisme = BooleanField(naam="heeftAntiVandalisme",
                                                label="heeft anti-vandalisme",
                                                objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftAntiVandalisme",
                                                definition="Is het een antivandalisme type verlichtingstoestel?",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Is het een antivandalisme type verlichtingstoestel?"""

        self.heeftSperfilter = BooleanField(naam="heeftSperfilter",
                                            label="heeft sperfilter",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftSperfilter",
                                            definition="Is er een sperfilter aanwezig?",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Is er een sperfilter aanwezig?"""
