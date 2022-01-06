from OTLModel.Classes.SelNietSelLus import SelNietSelLus
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVriLusFunctie import KlVriLusFunctie
from OTLModel.Datatypes.KlVriLusSoortvoertuig import KlVriLusSoortvoertuig


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietSelectieveDetectielus(SelNietSelLus):
    """Een niet-selectieve detectielus werkt onder invloed van een wijziging in de zelfinductie van een lus in het wegdek wanneer het metaal van een voertuig binnen het gevoeligheidsgebied van de lus komt. """

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.functie = KeuzelijstField(naam="functie",
                                       label="functie",
                                       lijst=KlVriLusFunctie(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.functie",
                                       definition="Type niet-selectieve detectielus bv. file, afstand, hiaat,...",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Type niet-selectieve detectielus bv. file, afstand, hiaat,..."""

        self.isMotorgevoelig = BooleanField(naam="isMotorgevoelig",
                                            label="is motorgevoelig",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isMotorgevoelig",
                                            definition="Geeft aan of de lus motorgevoelig is of niet.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Geeft aan of de lus motorgevoelig is of niet."""

        self.isRichtingsgevoelig = BooleanField(naam="isRichtingsgevoelig",
                                                label="is richtingsgevoelig",
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.isRichtingsgevoelig",
                                                definition="Is de detectielus gevoelig voor de richting waarin het voertuig het gevoeligheidsgebied van de lus binnenkomt?",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Is de detectielus gevoelig voor de richting waarin het voertuig het gevoeligheidsgebied van de lus binnenkomt?"""

        soortVoertuigField = KeuzelijstField(naam="soortVoertuig",
                                             label="soort voertuig",
                                             lijst=KlVriLusSoortvoertuig(),
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#NietSelectieveDetectielus.soortVoertuig",
                                             definition="Type voertuig dat de detectielus volgens zijn instellingen kan detecteren.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        self.soortVoertuig = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=soortVoertuigField)
        """Type voertuig dat de detectielus volgens zijn instellingen kan detecteren."""
