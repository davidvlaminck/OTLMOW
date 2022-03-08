import warnings

from OTLMOW.ModelGenerator.BaseClasses.GeldigeRelatie import GeldigeRelatie
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.ModelGenerator.BaseClasses.Singleton import Singleton


class RelatieValidator:
    def __init__(self, relatieLijst):
        self.dictByDoelBronRelatie = {}
        self.dictByBronDoelRelatie = {}
        self.fillValidatorDictsForEfficientSearch(relatieLijst)

    def enableValidateRelatieOnRelatieInteractor(self):
        def loadGeldigeRelaties(selfObject):
            geldigeRelatiesList = self.getGeldigeRelatiesByBronOrDoel(selfObject.typeURI)
            selfObject._geldigeRelaties = tuple(i for i in geldigeRelatiesList)
            selfObject._relatieValidatieMogelijk = True

        RelatieInteractor._loadGeldigeRelaties = loadGeldigeRelaties

    def fillValidatorDictsForEfficientSearch(self, relatieLijst: [GeldigeRelatie]):
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

    def validateRelatieByURI(self, bron, doel, relatieType):
        try:
            rel = self.dictByBronDoelRelatie[bron.typeURI][doel.typeURI][relatieType.typeURI]
            if rel.deprecated_version != '':
                warnings.warn(message=f'the relation of type {rel.relatie} between assets of types {rel.bron} and {rel.doel} is deprecated since version {rel.deprecated_version}',
                              category=DeprecationWarning)
            return self.dictByBronDoelRelatie[bron.typeURI][doel.typeURI][relatieType.typeURI] is not None
        except KeyError:
            return False

    def getGeldigeRelatiesByBronOrDoel(self, bronOfDoelUri: str):
        relaties = []
        if bronOfDoelUri in self.dictByBronDoelRelatie:
            for d in self.dictByBronDoelRelatie[bronOfDoelUri].values():
                relaties.extend(d.values())
        if bronOfDoelUri in self.dictByDoelBronRelatie:
            for d in self.dictByDoelBronRelatie[bronOfDoelUri].values():
                relaties.extend(d.values())
        return relaties
