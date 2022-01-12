# coding=utf-8
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OTLClassCreator. To modify: extend, do not edit
class VentilatieAfsluitklep(AIMObject):
    """Constructie voor het fysiek afsluiten van een ventilatieschacht die verhindert dat luchtstromen van de (dwars)ventilatie door de schachten gaan."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftManueleBediening = BooleanField(naam="heeftManueleBediening",
                                                  label="Heeft manuele bediening",
                                                  objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VentilatieAfsluitklep.heeftManueleBediening",
                                                  definition="Geeft aan of de afsluitklep manueel kan bediend worden.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Geeft aan of de afsluitklep manueel kan bediend worden."""
