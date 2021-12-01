from ModelGenerator.BaseClasses.AbstractRelatieInteractor import AbstractRelatieInteractor
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLClasses.Verification.RelatieObject import RelatieObject


class GeldigeRelatie:
    relatie: RelatieObject
    doel: AbstractRelatieInteractor
    richting: RelatieRichting

    def __init__(self, relatie: RelatieObject, doel: AbstractRelatieInteractor, richting: RelatieRichting):
        if not(isinstance(relatie, RelatieObject)):
            raise TypeError("parameter relatie is geen relatieObject")
        if not(isinstance(doel, AbstractRelatieInteractor)):
            raise TypeError("parameter doel is geen AbstractRelatieInteractor")
        if not(isinstance(richting, RelatieRichting)):
            raise TypeError("parameter richting is geen RelatieRichting")
        self.relatie = relatie
        self.doel = doel
        self.richting = richting
