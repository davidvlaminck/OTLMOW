from abc import abstractmethod, ABC

from OTLModel.BaseClasses.WKTField import WKTField


class OTLAsset(ABC):
    @abstractmethod
    def __init__(self):
        self.geometry = WKTField(naam='geometry',
                                 label='geometry',
                                 uri='https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
                                 definition='geometry voor DAVIE',
                                 constraints='',
                                 usagenote='',
                                 deprecated_version='')
