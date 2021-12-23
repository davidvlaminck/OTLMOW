from OTLModel.Classes.DNBMeter import DNBMeter


# Generated with OTLClassCreator
class EnergiemeterDNBPiek(DNBMeter):
    """Toestel dat eigendom is van de distributienetbeheerder en in de installatie van de asset beheerder geplaatst wordt voor het meten van piekvermogens."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNBPiek"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
