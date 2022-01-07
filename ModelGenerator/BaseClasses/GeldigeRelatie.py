from OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLModel.Classes.RelatieObject import RelatieObject


class GeldigeRelatie:
    bron: type
    doel: type
    relatie: type

    def __init__(self, bron: type, doel: type, relatie: type):
        relatieInstance = relatie()
        if not(isinstance(relatieInstance, RelatieObject)):
            raise TypeError("parameter relatie is geen RelatieObject")
        doelInstance = doel()
        if not(isinstance(doelInstance, RelatieInteractor)):
            raise TypeError("parameter doel is geen AbstractRelatieInteractor")
        bronInstance = bron()
        if not (isinstance(bronInstance, RelatieInteractor)):
            raise TypeError("parameter bron is geen AbstractRelatieInteractor")

        self.relatie = relatie
        self.doel = doel
        self.bron = bron
