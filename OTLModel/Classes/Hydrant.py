# coding=utf-8
from OTLModel.Classes.Brandvoorziening import Brandvoorziening
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlHydrantKoppeling import KlHydrantKoppeling
from OTLModel.Datatypes.KwantWrdInInch import KwantWrdInInch


# Generated with OTLClassCreator. To modify: extend, do not edit
class Hydrant(Brandvoorziening):
    """Aftappunt van de brandleiding bedoeld voor de brandweer. Ook brandkraan genoemd."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.diameter = KwantWrdInInch()
        """Diameter van het aftappunt."""
        self.diameter.naam = "diameter"
        self.diameter.label = "diameter"
        self.diameter.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.diameter"
        self.diameter.definition = "Diameter van het aftappunt."
        self.diameter.constraints = ""
        self.diameter.usagenote = ""
        self.diameter.deprecated_version = ""

        self.heeftEigenAfsluitkraan = BooleanField(naam="heeftEigenAfsluitkraan",
                                                   label="heeft eigen afsluitkraan",
                                                   objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.heeftEigenAfsluitkraan",
                                                   definition="Geeft aan of de hydrant ter plaatse kan afgesloten/opengezet kan worden.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Geeft aan of de hydrant ter plaatse kan afgesloten/opengezet kan worden."""

        self.heeftIsolatie = BooleanField(naam="heeftIsolatie",
                                          label="heeft isolatie",
                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.heeftIsolatie",
                                          definition="Geeft aan of de hydrant voorzien is van eigen isolatie.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Geeft aan of de hydrant voorzien is van eigen isolatie."""

        self.koppeling = KeuzelijstField(naam="koppeling",
                                         label="koppeling",
                                         lijst=KlHydrantKoppeling(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hydrant.koppeling",
                                         definition="Aard van de koppeling voor aansluiting van een aftapping.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Aard van de koppeling voor aansluiting van een aftapping."""
