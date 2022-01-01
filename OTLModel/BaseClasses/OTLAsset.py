from abc import abstractmethod, ABC


class OTLAsset(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # TODO add geometry and inherit from OTL Object instead