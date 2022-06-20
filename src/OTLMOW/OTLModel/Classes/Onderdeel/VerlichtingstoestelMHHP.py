# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Verlichtingstoestel import Verlichtingstoestel
from OTLMOW.OTLModel.Classes.Abstracten.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelMHHP(Verlichtingstoestel, VerlichtingstoestelConnector):
    """Het geheel van de metaalhalogenide lamp (MHHP), voorschakelapparatuur en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.armatuurkleur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.',
                                           owner=self)

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelMHHP.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?',
                                                 owner=self)

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
