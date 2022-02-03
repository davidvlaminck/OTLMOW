# coding=utf-8
from OTLMOW.OTLModel.Classes.DNBMeter import DNBMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDNBPiek(DNBMeter):
    """Toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor het meten van piekvermogens."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNBPiek'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
