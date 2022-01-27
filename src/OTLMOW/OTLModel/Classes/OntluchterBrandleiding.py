# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Brandvoorziening import Brandvoorziening


# Generated with OTLClassCreator. To modify: extend, do not edit
class OntluchterBrandleiding(Brandvoorziening):
    """Klep in de brandleiding die toelaat de leiding te ontluchten bij een droge blusleiding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OntluchterBrandleiding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
