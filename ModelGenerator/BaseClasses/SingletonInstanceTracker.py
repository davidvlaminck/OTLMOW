from ModelGenerator.BaseClasses.RelatieValidator import RelatieValidator
from ModelGenerator.BaseClasses.Singleton import Singleton
from OTLModel.Verification.GeldigeRelatieLijst import GeldigeRelatieLijst


class SingletonInstanceTracker(metaclass=Singleton):
    def getValidator(self):
        validator = RelatieValidator(GeldigeRelatieLijst())

        return validator
