from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCADOMerk import KlCADOMerk
from OTLModel.Datatypes.KlCADOModelnaam import KlCADOModelnaam
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Calamiteitendoorsteek(AIMNaamObject):
    """Een calamiteitendoorsteek, afgekort CADO, is een mechanische constructie voor het opklappen van een deel van de vangrail in de middenberm van een weg. Het primaire doel van de calamiteitendoorsteek is het doorlaten van hulpverleningsvoertuigen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isDubbelArmig = BooleanField(naam="isDubbelArmig",
                                          label="is dubbelarmig",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.isDubbelArmig",
                                          definition="Aanduiding of de calamiteitendoorsteek dubbel armig is.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Aanduiding of de calamiteitendoorsteek dubbel armig is."""

        self.lengte = KwantWrdInMeter()
        """De totale lengte van de calamiteitendoorsteek constructie."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.lengte"
        self.lengte.definition = "De totale lengte van de calamiteitendoorsteek constructie."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlCADOMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.merk",
                                    definition="Het merk van de calamiteitendoorsteek.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de calamiteitendoorsteek."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlCADOModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.modelnaam",
                                         definition="De modelnaam van de calamiteitendoorsteek.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van de calamiteitendoorsteek."""

        self.technischeFiche = DtcDocument()
        """De technische fiche van de calamiteitendoorsteek."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Calamiteitendoorsteek.technischeFiche"
        self.technischeFiche.definition = "De technische fiche van de calamiteitendoorsteek."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
