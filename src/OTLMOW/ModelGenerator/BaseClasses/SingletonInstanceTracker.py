from src.OTLMOW.OTLModel import GeldigeRelatieLijst
from src.OTLMOW.ModelGenerator.BaseClasses import RelatieValidator
from src.OTLMOW.ModelGenerator.BaseClasses import Singleton



class SingletonInstanceTracker(metaclass=Singleton):
    def getValidator(self):
        validator = RelatieValidator(GeldigeRelatieLijst())

        return validator
