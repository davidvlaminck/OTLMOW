from abc import abstractmethod

from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting


class RelatieInteractor:
    @abstractmethod
    def __init__(self):
        pass

    _geldigeRelaties = ()
    _relatieValidatieMogelijk = False

    def _loadGeldigeRelaties(self):
        pass

    def _validateRelatiePossible(self, doelObject, relatieType: type, relatieRichting: RelatieRichting):
        if not self._relatieValidatieMogelijk:
            raise NotImplementedError("initialize a RelatieValidator first")
        if relatieRichting == relatieRichting.BRON_DOEL:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.bron == type(self) and geldigeRelatie.doel == type(
                        doelObject) and geldigeRelatie.relatie == relatieType:
                    return True
        elif relatieRichting == relatieRichting.DOEL_BRON:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.doel == type(self) and geldigeRelatie.bron == type(
                        doelObject) and geldigeRelatie.relatie == relatieType:
                    return True
        return False
