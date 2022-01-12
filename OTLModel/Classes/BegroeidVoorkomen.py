# coding=utf-8
from abc import abstractmethod
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcVegetatieSoortnaam import DtcVegetatieSoortnaam
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlTaludWaarde import KlTaludWaarde
from OTLModel.Datatypes.KlVegetatieDrassigheid import KlVegetatieDrassigheid
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class BegroeidVoorkomen(AIMObject):
    """Abstracte die alle gemeenschappelijke eigenschappen omtrent begroeid voorkomen opsomt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self.breedte = KwantWrdInMeter()
        """De afstand van het begroeide oppervlak dwars op de as van de (water)weg."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.breedte"
        self.breedte.definition = "De afstand van het begroeide oppervlak dwars op de as van de (water)weg."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""

        self.drassigheid = KeuzelijstField(naam="drassigheid",
                                           label="drassigheid",
                                           lijst=KlVegetatieDrassigheid(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.drassigheid",
                                           definition="Mate waarin de bodem verzadigd is met water. De drassigheid geeft hierbij aan in welke mate de normale werking van types machines zou kunnen verstoord worden.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Mate waarin de bodem verzadigd is met water. De drassigheid geeft hierbij aan in welke mate de normale werking van types machines zou kunnen verstoord worden."""

        self.heeftObstakels = BooleanField(naam="heeftObstakels",
                                           label="heeft obstakels",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.heeftObstakels",
                                           definition="Eigenschap die aangeeft of er binnen het beheerdeel al dan niet objecten voorkomen die de vrije werking van machines of andere werktuigen kan verhinderen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Eigenschap die aangeeft of er binnen het beheerdeel al dan niet objecten voorkomen die de vrije werking van machines of andere werktuigen kan verhinderen."""

        self.lengte = KwantWrdInMeter()
        """De afstand van het begroeide oppervlak evenwijdig met de as van de (water)weg."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.lengte"
        self.lengte.definition = "De afstand van het begroeide oppervlak evenwijdig met de as van de (water)weg."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.oppervlakte = KwantWrdInVierkanteMeter()
        """De oppervlakte van het begroeide oppervlak in vierkante meter."""
        self.oppervlakte.naam = "oppervlakte"
        self.oppervlakte.label = "oppervlakte"
        self.oppervlakte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.oppervlakte"
        self.oppervlakte.definition = "De oppervlakte van het begroeide oppervlak in vierkante meter."
        self.oppervlakte.constraints = ""
        self.oppervlakte.usagenote = ""
        self.oppervlakte.deprecated_version = ""

        soortField = DtcVegetatieSoortnaam()
        soortField.naam = "soort"
        soortField.label = "soort"
        soortField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.soort"
        soortField.definition = "Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven."
        soortField.constraints = ""
        soortField.usagenote = ""
        soortField.deprecated_version = ""
        self.soort = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=soortField)
        """Met deze eigenschap worden de Nederlandse soortnaam, wetenschappelijke soortnaam en de soortcode van de meest voorkomende soorten binnen het begroeid oppervlak weergegeven."""

        self.taludwaarde = KeuzelijstField(naam="taludwaarde",
                                           label="taludwaarde",
                                           lijst=KlTaludWaarde(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BegroeidVoorkomen.taludwaarde",
                                           definition="Een talud is het kunstmatig gedeelte van een vlak van de wegbaan, dijken, spoorbanen, vestingswerken, ... dat een helling (min. 20%, max 80% voor kunstmatig verharde taluds) vertoont en bedoeld voor het opvangen van een hoogteverschil.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Een talud is het kunstmatig gedeelte van een vlak van de wegbaan, dijken, spoorbanen, vestingswerken, ... dat een helling (min. 20%, max 80% voor kunstmatig verharde taluds) vertoont en bedoeld voor het opvangen van een hoogteverschil."""
