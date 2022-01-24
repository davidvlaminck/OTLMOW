# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bebakening import Bebakening


# Generated with OTLClassCreator. To modify: extend, do not edit
class ReflectorInLijnvormigElement(Bebakening):
    """Een reflector dat deel uitmaakt van een constructie met als doel de zichtbaarheid van deze constructie te verhogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ReflectorInLijnvormigElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
