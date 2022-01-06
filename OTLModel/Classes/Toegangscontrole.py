# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlToegangscontroleSleuteltype import KlToegangscontroleSleuteltype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Toegangscontrole(AIMNaamObject):
    """Component voor controle van de toegang tot een ruimte of behuizing."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftBadgelezer = BooleanField(naam="heeftBadgelezer",
                                            label="heeft badgelezer",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftBadgelezer",
                                            definition="Geeft aan of de toegangscontrole uitgerust is met een badgelezer.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Geeft aan of de toegangscontrole uitgerust is met een badgelezer."""

        self.heeftSlotMetAfstandsbediening = BooleanField(naam="heeftSlotMetAfstandsbediening",
                                                          label="heeft slot met afstandsbediening",
                                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.heeftSlotMetAfstandsbediening",
                                                          definition="Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening.",
                                                          constraints="",
                                                          usagenote="",
                                                          deprecated_version="")
        """Geeft aan of het objecttype waaraan de toegangscontrole bevestigd is, kan geopend worden via een slot met afstandsbediening."""

        self.sleutelType = KeuzelijstField(naam="sleutelType",
                                           label="type sleutel",
                                           lijst=KlToegangscontroleSleuteltype(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Toegangscontrole.sleutelType",
                                           definition="De soort sleutel die wordt gebruikt om de toegang te regelen.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De soort sleutel die wordt gebruikt om de toegang te regelen."""
