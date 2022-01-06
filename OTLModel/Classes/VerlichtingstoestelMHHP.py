# coding=utf-8
from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelMHHP(VerlichtingstoestelConnector, Verlichtingstoestel):
    """Het geheel van de metaalhalogenide lamp (MHHP), voorschakelapparatuur en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VerlichtingstoestelConnector.__init__(self)
        Verlichtingstoestel.__init__(self)

        self.armatuurkleur = DteKleurRAL()
        """De kleur van de zichtbare buitenkant van het verlichtingstoestel."""
        self.armatuurkleur.naam = "armatuurkleur"
        self.armatuurkleur.label = "armatuurkleur"
        self.armatuurkleur.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.armatuurkleur"
        self.armatuurkleur.definition = "De kleur van de zichtbare buitenkant van het verlichtingstoestel."
        self.armatuurkleur.constraints = ""
        self.armatuurkleur.usagenote = ""
        self.armatuurkleur.deprecated_version = ""

        self.heeftAntiVandalisme = BooleanField(naam="heeftAntiVandalisme",
                                                label="heeft anti vandalisme",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.heeftAntiVandalisme",
                                                definition="Is het een antivandalisme type verlichtingstoestel?",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Is het een antivandalisme type verlichtingstoestel?"""
