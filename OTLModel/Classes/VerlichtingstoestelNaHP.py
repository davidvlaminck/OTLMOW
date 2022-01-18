# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelNaHP(VerlichtingstoestelConnector, Verlichtingstoestel, AttributeInfo):
    """Het geheel van de natrium hoge druk lamp (NaHP) en de behuizing die werden samengesteld met als doel:
* de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
* de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
* het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)

        self._armatuurkleur = OTLAttribuut(field=DteKleurRAL,
                                           naam='armatuurkleur',
                                           label='armatuurkleur',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.armatuurkleur',
                                           definition='De kleur van de zichtbare buitenkant van het verlichtingstoestel.')

        self._heeftAntiVandalisme = OTLAttribuut(field=BooleanField,
                                                 naam='heeftAntiVandalisme',
                                                 label='heeft anti-vandalisme',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftAntiVandalisme',
                                                 definition='Is het een antivandalisme type verlichtingstoestel?')

        self._heeftSperfilter = OTLAttribuut(field=BooleanField,
                                             naam='heeftSperfilter',
                                             label='heeft sperfilter',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelNaHP.heeftSperfilter',
                                             definition='Is er een sperfilter aanwezig?')

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
    def heeftSperfilter(self):
        """Is er een sperfilter aanwezig?"""
        return self._heeftSperfilter.waarde

    @heeftSperfilter.setter
    def heeftSperfilter(self, value):
        self._heeftSperfilter.set_waarde(value, owner=self)
