# coding=utf-8
from OTLModel.Classes.Buis import Buis
from OTLModel.Datatypes.IntegerField import IntegerField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRioleringsbuisFunctie import KlRioleringsbuisFunctie
from OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal
from OTLModel.Datatypes.KlSterktereeks import KlSterktereeks


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsbuis(Buis):
    """Ondergronds kanaal of pijp voor gravitaire afvoer van water."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalAfgedichteAansluitingen = IntegerField(naam="aantalAfgedichteAansluitingen",
                                                          label="Aantal afgedichte aansluitingen",
                                                          objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.aantalAfgedichteAansluitingen",
                                                          definition="De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        """De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis."""

        self.functie = KeuzelijstField(naam="functie",
                                       label="functie",
                                       lijst=KlRioleringsbuisFunctie(),
                                       objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.functie",
                                       definition="Bepaalt de functie van de rioleringsbuis.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Bepaalt de functie van de rioleringsbuis."""

        self.materiaal = KeuzelijstField(naam="materiaal",
                                         label="materiaal",
                                         lijst=KlRioleringsbuisMateriaal(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.materiaal",
                                         definition="Bepaalt het materiaal van de rioleringsbuis.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Bepaalt het materiaal van de rioleringsbuis."""

        self.sterktereeks = KeuzelijstField(naam="sterktereeks",
                                            label="sterktereeks",
                                            lijst=KlSterktereeks(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.sterktereeks",
                                            definition="De stabiliteitsklasse van de buis.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """De stabiliteitsklasse van de buis."""
