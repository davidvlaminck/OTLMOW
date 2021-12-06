from ModelGenerator.BaseClasses.RelatieInteractor import RelatieInteractor
from ModelGenerator.BaseClasses.Singleton import Singleton
from OTLClasses.Verification.GeldigeRelatieLijst import GeldigeRelatieLijst


class RelatieValidator(metaclass=Singleton):
    def __init__(self, relatieLijst: GeldigeRelatieLijst):
        self.dictByDoelBronRelatie = {}
        self.dictByBronDoelRelatie = {}
        self.fillValidatorDictsForEfficientSearch(relatieLijst)
        self.enableValidateRelatieOnRelatieInteractor()

    def enableValidateRelatieOnRelatieInteractor(self):
        def loadGeldigeRelaties(selfObject):
            geldigeRelatiesList = self.getGeldigeRelatiesByBronOrDoel(selfObject)
            selfObject._geldigeRelaties = tuple(i for i in geldigeRelatiesList)

        RelatieInteractor.loadGeldigeRelaties = loadGeldigeRelaties
        RelatieInteractor._relatieValidatieMogelijk = True

    def fillValidatorDictsForEfficientSearch(self, relatieLijst):
        for rel in relatieLijst.lijst:
            if rel.bron not in self.dictByBronDoelRelatie:
                self.dictByBronDoelRelatie[rel.bron] = {}
            if rel.doel not in self.dictByBronDoelRelatie[rel.bron]:
                self.dictByBronDoelRelatie[rel.bron][rel.doel] = {}
            self.dictByBronDoelRelatie[rel.bron][rel.doel][rel.relatie] = rel
        for rel in relatieLijst.lijst:
            if rel.doel not in self.dictByDoelBronRelatie:
                self.dictByDoelBronRelatie[rel.doel] = {}
            if rel.bron not in self.dictByDoelBronRelatie[rel.doel]:
                self.dictByDoelBronRelatie[rel.doel][rel.bron] = {}
            self.dictByDoelBronRelatie[rel.doel][rel.bron][rel.relatie] = rel

    def validateRelatie(self, bron: RelatieInteractor, doel: RelatieInteractor, relatieType: type):
        try:
            return self.dictByBronDoelRelatie[type(bron)][type(doel)][relatieType] is not None
        except KeyError:
            return False

    def getGeldigeRelatiesByBronOrDoel(self, bronOfDoel: RelatieInteractor):
        relaties = []
        bronOfDoelType = type(bronOfDoel)
        if bronOfDoelType in self.dictByBronDoelRelatie:
            for d in self.dictByBronDoelRelatie[bronOfDoelType].values():
                relaties.extend(d.values())
        if bronOfDoelType in self.dictByDoelBronRelatie:
            for d in self.dictByDoelBronRelatie[bronOfDoelType].values():
                relaties.extend(d.values())
        return relaties
