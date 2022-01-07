from OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from ModelGenerator.BaseClasses.Singleton import Singleton


class RelatieValidator(metaclass=Singleton):
    def __init__(self, relatieLijst):
        self.dictByDoelBronRelatie = {}
        self.dictByBronDoelRelatie = {}
        self.fillValidatorDictsForEfficientSearch(relatieLijst)
        self.enableValidateRelatieOnRelatieInteractor()

    def enableValidateRelatieOnRelatieInteractor(self):
        def loadGeldigeRelaties(selfObject):
            geldigeRelatiesList = self.getGeldigeRelatiesByBronOrDoel(selfObject)
            selfObject._geldigeRelaties = tuple(i for i in geldigeRelatiesList)

        RelatieInteractor._loadGeldigeRelaties = loadGeldigeRelaties
        RelatieInteractor._relatieValidatieMogelijk = True

    def fillValidatorDictsForEfficientSearch(self, relatieLijst):
        for rel in relatieLijst.lijst:
            if rel.bron not in self.dictByBronDoelRelatie:
                self.dictByBronDoelRelatie[rel.bron] = {}
            if rel.doel not in self.dictByBronDoelRelatie[rel.bron]:
                self.dictByBronDoelRelatie[rel.bron][rel.doel] = {}
            self.dictByBronDoelRelatie[rel.bron][rel.doel][rel.relatie] = rel
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

    def validateRelatieByURI(self, bron, doel, relatieType):
        try:
            return self.dictByBronDoelRelatie[bron.typeURI][doel.typeURI][relatieType.typeURI] is not None
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
