# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luchtkwaliteitsensor(NaampadObject):
    """Installatie voor het meten van verschillende aspecten van de luchtkwaliteit in tunnels tussen twee punten op basis van de onderbrekingen in een signaal dat tussen die twee punten reist."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Luchtkwaliteitsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
