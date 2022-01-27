# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class SluitAanOp(DirectioneleRelatie):
    """Deze relatie geeft aan hoe 2 onderdelen in horizontale zin elkaar opvolgen. Dit wordt gebruikt om een topologisch netwerk op te bouwen. Enkel in gebruik bij afschermende constructies en riolering/waterlopen. Deze relatie heeft steeds een richting van het opwaartse naar het afwaartse onderdeel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
