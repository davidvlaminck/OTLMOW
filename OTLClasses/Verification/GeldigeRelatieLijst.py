from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLClasses.Verification.Laagspanningsbord import Laagspanningsbord
from OTLClasses.Verification.Aftakking import Aftakking
from OTLClasses.Verification.Bevestiging import Bevestiging
from OTLClasses.Verification.Contactor import Contactor
from OTLClasses.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLClasses.Verification.Hoofdschakelaar import Hoofdschakelaar
from OTLClasses.Verification.Stroomkring import Stroomkring
from OTLClasses.Verification.Sturing import Sturing
from OTLClasses.Verification.Voedt import Voedt


class GeldigeRelatieLijst:
    def __init__(self):
        self.lijst = [
            GeldigeRelatie(EnergiemeterAWV, Aftakking, Voedt),
            GeldigeRelatie(Stroomkring, Aftakking, Sturing),
            GeldigeRelatie(Aftakking, Stroomkring, Sturing),
            GeldigeRelatie(Hoofdschakelaar, Aftakking, Voedt),
            GeldigeRelatie(Aftakking, Hoofdschakelaar, Voedt),
            GeldigeRelatie(Hoofdschakelaar, EnergiemeterAWV, Voedt),
            GeldigeRelatie(Stroomkring, Contactor, Voedt),
            GeldigeRelatie(Laagspanningsbord, Contactor, Bevestiging),
            GeldigeRelatie(Contactor, Laagspanningsbord, Bevestiging),
            GeldigeRelatie(Laagspanningsbord, Stroomkring, Bevestiging),
            GeldigeRelatie(Stroomkring, Laagspanningsbord, Bevestiging),
            GeldigeRelatie(Laagspanningsbord, Aftakking, Bevestiging),
            GeldigeRelatie(Aftakking, Laagspanningsbord, Bevestiging),
        ]
