from abc import abstractmethod

from OTLModel.Verification.RelatieObject import RelatieObject


class DirectioneleRelatie(RelatieObject):
    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)
