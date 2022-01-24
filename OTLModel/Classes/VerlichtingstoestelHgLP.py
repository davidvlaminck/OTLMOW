# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.VerlichtingstoestelConnector import VerlichtingstoestelConnector
from OTLModel.Classes.Verlichtingstoestel import Verlichtingstoestel


# Generated with OTLClassCreator. To modify: extend, do not edit
class VerlichtingstoestelHgLP(VerlichtingstoestelConnector, Verlichtingstoestel):
    """Het geheel van de lagedruk kwik lamp (of fluorescentielamp) (HgLP),, voorschakelapparatuur en de behuizing die werden samengesteld met als doel:
 * de lichtstroom van de lichtbronnen hoofdzakelijk op het te verlichten oppervlak (doorlopende wegsectie, conflictgebied,...) te richten, teneinde de zichtbaarheid te verhogen;
 * de lichtstroom te beheersen zodat de weggebruikers niet verblind worden en de lichthinder beperkt wordt;
 * het optisch systeem, de lichtbronnen en de hulpapparatuur tegen uitwendige invloeden te beschermen"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VerlichtingstoestelHgLP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Verlichtingstoestel.__init__(self)
        VerlichtingstoestelConnector.__init__(self)
