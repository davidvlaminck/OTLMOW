# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from src.OTLMOW.OTLModel.Datatypes.DtcBetonspecificaties import DtcBetonspecificaties
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KlUitvoeringsmethode import KlUitvoeringsmethode


# Generated with OTLClassCreator. To modify: extend, do not edit
class BetonnenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van betonnen constructie-elementen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self._betonspecificaties = OTLAttribuut(field=DtcBetonspecificaties,
                                                naam='betonspecificaties',
                                                label='betonspecificaties',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.betonspecificaties',
                                                definition='Eigenschappen van het gebruikte beton.')

        self._uitvoeringsmethode = OTLAttribuut(field=KlUitvoeringsmethode,
                                                naam='uitvoeringsmethode',
                                                label='uitvoeringsmethode',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.uitvoeringsmethode',
                                                definition='Op welke manier het beton wordt aangebracht.')

        self._wapeningsplan = OTLAttribuut(field=DtcDocument,
                                           naam='wapeningsplan',
                                           label='wapeningsplan',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.wapeningsplan',
                                           definition='Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters).')

    @property
    def betonspecificaties(self):
        """Eigenschappen van het gebruikte beton."""
        return self._betonspecificaties.waarde

    @betonspecificaties.setter
    def betonspecificaties(self, value):
        self._betonspecificaties.set_waarde(value, owner=self)

    @property
    def uitvoeringsmethode(self):
        """Op welke manier het beton wordt aangebracht."""
        return self._uitvoeringsmethode.waarde

    @uitvoeringsmethode.setter
    def uitvoeringsmethode(self, value):
        self._uitvoeringsmethode.set_waarde(value, owner=self)

    @property
    def wapeningsplan(self):
        """Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters)."""
        return self._wapeningsplan.waarde

    @wapeningsplan.setter
    def wapeningsplan(self, value):
        self._wapeningsplan.set_waarde(value, owner=self)
