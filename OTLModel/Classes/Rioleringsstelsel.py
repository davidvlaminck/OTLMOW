# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRioleringStelsel import KlRioleringStelsel


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsstelsel(AIMObject):
    """De groepering van de objecten die behoren tot de riolering."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.systeemtype = KeuzelijstField(naam="systeemtype",
                                           label="systeemtype",
                                           lijst=KlRioleringStelsel(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Rioleringsstelsel.systeemtype",
                                           definition="Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Geeft aan wat voor afvoerwater er door de riolering afgevoerd wordt."""
