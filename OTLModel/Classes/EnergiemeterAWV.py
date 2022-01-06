from OTLModel.Classes.Energiemeter import Energiemeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterAWV(Energiemeter):
    """Toestel voor multifunctionele stroom- en spanningsmetingen en logging, die via een van de courante standaardkoppelvlakken (Euridis, RS485, Modbus, ...) wordt aangesloten om lokaal of op afstand te kunnen uitlezen en zodoende het energieverbruik te kunnen opvolgen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
