from abc import abstractmethod

from ModelGenerator.BaseClasses.OTLAsset import OTLAsset
from ModelGenerator.BaseClasses.StringField import StringField
from OTLClasses.Verification.AIMDBStatus import AIMDBStatus
from OTLClasses.Verification.AIMToestand import AIMToestand
from ModelGenerator.BaseClasses.RelatieInteractor import RelatieInteractor


class AIMObject(AIMToestand, OTLAsset, AIMDBStatus, RelatieInteractor):
    """Abstracte als de basisklasse voor alle uniek geïdentificeerde OTL objecten met de basiseigenschappen die elk OTL object minstens heeft."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMObject"

    notitie = StringField()
    """Extra notitie voor het object."""

    # TODO: incomplete: missing attributes

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

