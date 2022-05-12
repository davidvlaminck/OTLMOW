# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Cabine import Cabine
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.KlCabineLokaalKlasse import KlCabineLokaalKlasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class HSCabine(Cabine):
    """Een behuizing  bestemd voor het beschermen van elektrisch hoogspanningsmateriaal en het daarbij horende laagspanningsmateriaal en elektromechanische technieken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._lokaalKlasse = OTLAttribuut(field=KlCabineLokaalKlasse,
                                          naam='lokaalKlasse',
                                          label='lokaal klasse',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.lokaalKlasse',
                                          definition='Classificatie van de hoogspanningscabine als lokaal volgens Synergrid.',
                                          owner=self)

        self._vervaldatumVeiligheidshandschoenen = OTLAttribuut(field=DateField,
                                                                naam='vervaldatumVeiligheidshandschoenen',
                                                                label='vervaldatum veiligheidshandschoenen',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSCabine.vervaldatumVeiligheidshandschoenen',
                                                                definition='De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen.',
                                                                owner=self)

    @property
    def lokaalKlasse(self):
        """Classificatie van de hoogspanningscabine als lokaal volgens Synergrid."""
        return self._lokaalKlasse.get_waarde()

    @lokaalKlasse.setter
    def lokaalKlasse(self, value):
        self._lokaalKlasse.set_waarde(value, owner=self)

    @property
    def vervaldatumVeiligheidshandschoenen(self):
        """De datum waarop de huidige veiligheidshandschoenen in de hoogspanningscabine vervallen."""
        return self._vervaldatumVeiligheidshandschoenen.get_waarde()

    @vervaldatumVeiligheidshandschoenen.setter
    def vervaldatumVeiligheidshandschoenen(self, value):
        self._vervaldatumVeiligheidshandschoenen.set_waarde(value, owner=self)
