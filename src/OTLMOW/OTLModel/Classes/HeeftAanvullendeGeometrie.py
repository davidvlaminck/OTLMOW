# coding=utf-8
from OTLMOW.OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftAanvullendeGeometrie(DirectioneleRelatie):
    """Deze relatie legt een link tussen een object/onderdeel/installatie en een (bestands)bijlage waar een geometrie aan toegekend is. De richting loopt vanuit het fysiek object naar de bijlage met geometrie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftAanvullendeGeometrie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
