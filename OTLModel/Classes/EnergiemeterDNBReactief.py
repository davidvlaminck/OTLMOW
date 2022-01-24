# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.DNBMeter import DNBMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDNBReactief(DNBMeter):
    """Toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor het meten van het reactief vermogen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNBReactief'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
