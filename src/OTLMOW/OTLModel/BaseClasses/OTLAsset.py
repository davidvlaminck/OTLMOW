from abc import abstractmethod

from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject


class OTLAsset(OTLObject):
    @abstractmethod
    def __init__(self):
        super().__init__()
