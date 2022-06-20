# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.Kabelgeleiding import Kabelgeleiding


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelladder(Kabelgeleiding):
    """Een inrichting die ervoor zorgt dat een kabel beschermd is tegen beschadiging en/of op een gecontroleerde plaats blijft hangen of liggen. De kabelladder is een gerasterde constructie die doet denken aan een ladder, die toelaat om de kabels langs alle kanten te zien. Slechts langs één kant is de toegang tot de kabels fysiek onbelet."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelladder'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
