from ModelGenerator.BaseClasses.AbstractRelatieInteractor import AbstractRelatieInteractor
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLClasses.Verification.RelatieObject import RelatieObject


class GeldigeRelatie:
    relatie: type
    doel: type
    richting: RelatieRichting

    def __init__(self, relatie: type, doel: type, richting: RelatieRichting):
        relatieInstance = relatie()
        if not(isinstance(relatieInstance, RelatieObject)):
            raise TypeError("parameter relatie is geen relatieObject")
        doelInstance = doel()
        if not(isinstance(doelInstance, AbstractRelatieInteractor)):
            raise TypeError("parameter doel is geen AbstractRelatieInteractor")
        if not(isinstance(richting, RelatieRichting)):
            raise TypeError("parameter richting is geen RelatieRichting")
        self.relatie = relatie
        self.doel = doel
        self.richting = richting
