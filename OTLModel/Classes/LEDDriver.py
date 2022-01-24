# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlLEDDriverMerk import KlLEDDriverMerk
from OTLModel.Datatypes.KlLEDDriverModelnaam import KlLEDDriverModelnaam
from OTLModel.Datatypes.KlLEDDriverProtocol import KlLEDDriverProtocol
from OTLModel.Datatypes.KwantWrdInMilliAmpere import KwantWrdInMilliAmpere
from OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDDriver(AIMObject):
    """Een LED-driver is een elektronisch toestel dat de stroomtoevoer naar de LED's dimensioneert om de goede werking te verzekeren. Via de instelparameters van de driver kan uiteindelijk de lichtsterkte van de LED verlichting aangepast worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._maximaalVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                              naam='maximaalVermogen',
                                              label='maximaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaalVermogen',
                                              definition='Maximaal afgenomen vermogen van de driver en lamp samen (incl. verlies/verbruik van de driver zelf).')

        self._maximaleAanstuurstroom = OTLAttribuut(field=KwantWrdInMilliAmpere,
                                                    naam='maximaleAanstuurstroom',
                                                    label='maximale aanstuurstroom',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.maximaleAanstuurstroom',
                                                    definition='Maximale aanstuurstroom die de LED driver kan leveren.')

        self._merk = OTLAttribuut(field=KlLEDDriverMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.merk',
                                  definition='Het merk van de LED-driver.')

        self._modelnaam = OTLAttribuut(field=KlLEDDriverModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.modelnaam',
                                       definition='De modelnaam van de LED-driver.')

        self._protocol = OTLAttribuut(field=KlLEDDriverProtocol,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver.protocol',
                                      definition="Protocol gebruikt door de LED driver voor het aansturen van de LED's.")

    @property
    def maximaalVermogen(self):
        """Maximaal afgenomen vermogen van de driver en lamp samen (incl. verlies/verbruik van de driver zelf)."""
        return self._maximaalVermogen.waarde

    @maximaalVermogen.setter
    def maximaalVermogen(self, value):
        self._maximaalVermogen.set_waarde(value, owner=self)

    @property
    def maximaleAanstuurstroom(self):
        """Maximale aanstuurstroom die de LED driver kan leveren."""
        return self._maximaleAanstuurstroom.waarde

    @maximaleAanstuurstroom.setter
    def maximaleAanstuurstroom(self, value):
        self._maximaleAanstuurstroom.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de LED-driver."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de LED-driver."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def protocol(self):
        """Protocol gebruikt door de LED driver voor het aansturen van de LED's."""
        return self._protocol.waarde

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)
