# coding=utf-8
from OTLModel.Classes.Cabine import Cabine
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlCabineLokaalKlasse import KlCabineLokaalKlasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class HSCabine(Cabine):
    """Een behuizing  bestemd voor het beschermen van elektrisch hoogspanningsmateriaal en het daarbij horende laagspanningsmateriaal en elektromechanische technieken."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.lokaalKlasse = KeuzelijstField(naam="lokaalKlasse",
                                            label="lokaal klasse",
                                            lijst=KlCabineLokaalKlasse(),
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.lokaalKlasse",
                                            definition="Classificatie van de hoogspanningscabine als lokaal volgens Synergrid.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""

        self.vervaldatumVeiligheidshandschoenen = DateField(naam="vervaldatumVeiligheidshandschoenen",
                                                            label="vervaldatum veiligheidshandschoenen",
                                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.vervaldatumVeiligheidshandschoenen",
                                                            definition="De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen.",
                                                            constraints="",
                                                            usagenote="",
                                                            deprecated_version="")
        """De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen."""
