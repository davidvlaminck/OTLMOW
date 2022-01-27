# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVConsole(AIMNaamObject):
    """Een draagconstructie voor het ophangen van openbare wegverlichting op plaatsen waar er geen ruimte is voor verlichtingsmasten in de grond. Typisch wordt in dergelijke gevallen de draagconstructie met het verlichtingstoestel op hoogte bevestigd aan een gebouw of een andere constructie naast de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVConsole'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
