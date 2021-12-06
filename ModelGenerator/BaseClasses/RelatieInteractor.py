from abc import ABC

from ModelGenerator.BaseClasses.AbstractRelatieInteractor import AbstractRelatieInteractor
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting


class RelatieInteractor: # (AbstractRelatieInteractor)
    def __init__(self):
        pass

    _geldigeRelaties = ()
    _geldig = False

    def loadGeldigeRelaties(self):
        pass

    def validateRelatiePossible(self, doelObject, relatieType: type, relatieRichting: RelatieRichting):
        if not self._geldig:
            raise NotImplementedError("initialize relatieValidator first")
        if relatieRichting == relatieRichting.BRON_DOEL:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.bron == type(self) and geldigeRelatie.doel == type(doelObject) and geldigeRelatie.relatie == relatieType:
                    return True
        elif relatieRichting == relatieRichting.DOEL_BRON:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.doel == type(self) and geldigeRelatie.bron == type(doelObject) and geldigeRelatie.relatie == relatieType:
                    return True
        return False








