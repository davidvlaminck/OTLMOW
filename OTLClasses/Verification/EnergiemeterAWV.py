from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from ModelGenerator.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.Energiemeter import Energiemeter
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLClasses.Verification.Voedt import Voedt


class EnergiemeterAWV(Energiemeter):
    """Toestel voor multifunctionele stroom- en spanningsmetingen en logging, die via een van de courante standaardkoppelvlakken (Euridis, RS485, Modbus, ...) wordt aangesloten om lokaal of op afstand te kunnen uitlezen en zodoende het energieverbruik te kunnen opvolgen"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterAWV"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Energiemeter.__init__(self)
        #self.geldige_relaties.extend(super().geldige_relaties)
        #self.add_geldige_relatie(Voedt(), Aftakking(), RelatieRichting.BRON_DOEL)
        #self.add_geldige_relatie(Voedt, Hoofdschakelaar, RelatieRichting.DOEL_BRON)
        #self.add_geldige_relatie(Voedt, Stroomkring, RelatieRichting.DOEL_BRON)

    #geldige_relaties = [GeldigeRelatie(Voedt(), Aftakking(), RelatieRichting.BRON_DOEL)]






