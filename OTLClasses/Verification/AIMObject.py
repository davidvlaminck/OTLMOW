from abc import abstractmethod

from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from ModelGenerator.BaseClasses.StringField import StringField
from ModelGenerator.BaseClasses.URIField import AnyURIField
from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMToestand import AIMToestand
from ModelGenerator.BaseClasses.RelatieInteractor import RelatieInteractor


class AIMObject(AIMToestand, OTLAsset, AIMDBStatus, RelatieInteractor):
    """Abstracte als de basisklasse voor alle uniek geïdentificeerde OTL objecten met de basiseigenschappen die elk OTL object minstens heeft."""
    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    notitie = StringField()
    """Extra notitie voor het object."""

    # TODO: incomplete: missing attributes

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)
