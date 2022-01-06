from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPutRooster import KlPutRooster
from OTLModel.Datatypes.KlRoosterIndeling import KlRoosterIndeling
from OTLModel.Datatypes.KlRoosterOpeningswijze import KlRoosterOpeningswijze
from OTLModel.Datatypes.KlStraatkolkBakType import KlStraatkolkBakType
from OTLModel.Datatypes.KlStraatkolkType import KlStraatkolkType
from OTLModel.Datatypes.KlStraatkolkTypeUitlaat import KlStraatkolkTypeUitlaat


# Generated with OTLClassCreator. To modify: extend, do not edit
class Straatkolk(Put, PutRelatie):
    """De hemelwaterinlaatconstructie,meestal geplaatst in de straatgoot of watergreppel,waarlangs het hemelwater van de verhardingen wordt afgevoerd."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self.bakAfmetingen = DtcAfmetingBxlxhInMm()
        """De afmetingen van de bak van de straatkolk in mm."""
        self.bakAfmetingen.naam = "bakAfmetingen"
        self.bakAfmetingen.label = "bak afmetingen"
        self.bakAfmetingen.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.bakAfmetingen"
        self.bakAfmetingen.definition = "De afmetingen van de bak van de straatkolk in mm."
        self.bakAfmetingen.constraints = ""
        self.bakAfmetingen.usagenote = ""
        self.bakAfmetingen.deprecated_version = ""

        self.bakType = KeuzelijstField(naam="bakType",
                                       label="baktype",
                                       lijst=KlStraatkolkBakType(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.bakType",
                                       definition="Het type van bak van de straatkolk.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het type van bak van de straatkolk."""

        self.heeftAfdekplaatReukafsluiter = BooleanField(naam="heeftAfdekplaatReukafsluiter",
                                                         label="heeft afdekplaat reukafsluiter",
                                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.heeftAfdekplaatReukafsluiter",
                                                         definition="Dit attribuut geeft aan of de straatkolk een afdekplaat als reukafsluiter heeft.",
                                                         constraints="",
                                                         usagenote="",
                                                         deprecated_version="")
        """Dit attribuut geeft aan of de straatkolk een afdekplaat als reukafsluiter heeft."""

        self.isInfiltrerend = BooleanField(naam="isInfiltrerend",
                                           label="is infiltrerend",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.isInfiltrerend",
                                           definition="Wanneer de wanden van de straatkolk poreus zijn (en de straatkolk dus infiltrerend is), kan een deel van het water het water dat in de straatkolk komt rechtstreeks in de grond infiltreren.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Wanneer de wanden van de straatkolk poreus zijn (en de straatkolk dus infiltrerend is), kan een deel van het water het water dat in de straatkolk komt rechtstreeks in de grond infiltreren."""

        self.roosterIndeling = KeuzelijstField(naam="roosterIndeling",
                                               label="rooster indeling",
                                               lijst=KlRoosterIndeling(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.roosterIndeling",
                                               definition="Dit attribuut geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Dit attribuut geeft aan hoe het rooster ingedeeld is: met zijdelingse opvang of dat er sprake is van een 1-delig of 2-delig rooster."""

        self.roosterOpeningswijze = KeuzelijstField(naam="roosterOpeningswijze",
                                                    label="rooster openingswijze",
                                                    lijst=KlRoosterOpeningswijze(),
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.roosterOpeningswijze",
                                                    definition="Dit attribuut geeft de manier aan hoe het rooster geopend kan worden.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Dit attribuut geeft de manier aan hoe het rooster geopend kan worden."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlStraatkolkType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.type",
                                    definition="Het type van de straatkolk.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van de straatkolk."""

        self.typeUitlaat = KeuzelijstField(naam="typeUitlaat",
                                           label="type uitlaat ",
                                           lijst=KlStraatkolkTypeUitlaat(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Straatkolk.typeUitlaat",
                                           definition="Het type van uitlaat van de straatkolk.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Het type van uitlaat van de straatkolk."""
