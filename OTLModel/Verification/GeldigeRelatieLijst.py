from ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLModel.Verification.Laagspanningsbord import Laagspanningsbord
from OTLModel.Verification.Aftakking import Aftakking
from OTLModel.Verification.Bevestiging import Bevestiging
from OTLModel.Verification.Contactor import Contactor
from OTLModel.Verification.EnergiemeterAWV import EnergiemeterAWV
from OTLModel.Verification.Hoofdschakelaar import Hoofdschakelaar
from OTLModel.Verification.Stroomkring import Stroomkring
from OTLModel.Verification.Sturing import Sturing
from OTLModel.Verification.Voedt import Voedt


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
