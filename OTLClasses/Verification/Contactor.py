from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLClasses.Verification.AIMObject import AIMObject
from OTLClasses.Verification.Voedt import Voedt


class Contactor(AIMObject):
    """Toestel dat ter plaatse of op afstand aangestuurd wordt om (grote) vermogensstromen af te schakelen."""
    def __init__(self):
        pass
        #self.add_geldige_relatie(Voedt, type(self), RelatieRichting.BRON_DOEL)

    # TODO eigen attributen ontbreken

    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor"



