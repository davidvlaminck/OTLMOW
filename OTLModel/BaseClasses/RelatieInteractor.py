from abc import abstractmethod

from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting


class RelatieInteractor:
    typeURI = ''
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        pass

    _geldigeRelaties = ()
    _relatieValidatieMogelijk = False

    def _loadGeldigeRelaties(self):
        raise NotImplementedError("initialize a RelatieValidator first")

    def _validateRelatiePossible(self, doelObject, relatieType: type, relatieRichting: RelatieRichting):
        if not self._relatieValidatieMogelijk:
            self._loadGeldigeRelaties()
        if relatieRichting == relatieRichting.BRON_DOEL:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.bron == self.typeURI and geldigeRelatie.doel == doelObject.typeURI and geldigeRelatie.relatie == relatieType.typeURI:
                    return True
        elif relatieRichting == relatieRichting.DOEL_BRON:
            for geldigeRelatie in self._geldigeRelaties:
                if geldigeRelatie.doel == self.typeURI and geldigeRelatie.bron == doelObject.typeURI and geldigeRelatie.relatie == relatieType.typeURI:
                    return True
        return False
