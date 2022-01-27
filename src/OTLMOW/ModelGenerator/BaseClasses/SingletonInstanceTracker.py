from OTLMOW.OTLModel import GeldigeRelatieLijst
from OTLMOW.ModelGenerator.BaseClasses import RelatieValidator
from OTLMOW.ModelGenerator.BaseClasses import Singleton



class SingletonInstanceTracker(metaclass=Singleton):
    def getValidator(self):
        validator = RelatieValidator(GeldigeRelatieLijst())

        return validator
