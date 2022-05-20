# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcMarkeringOpvatting import DtcMarkeringOpvatting
from OTLMOW.OTLModel.Datatypes.DtcProductidentificatiecode import DtcProductidentificatiecode
from OTLMOW.OTLModel.Datatypes.KlKleurMarkering import KlKleurMarkering
from OTLMOW.OTLModel.Datatypes.KlMarkeringSoort import KlMarkeringSoort


# Generated with OTLClassCreator. To modify: extend, do not edit
class Markering(AIMObject, Signalisatie):
    """Abstracte als noemer voor de verschillende types van markeringen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        self._isHandwerk = OTLAttribuut(field=BooleanField,
                                        naam='isHandwerk',
                                        label='is handwerk',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isHandwerk',
                                        definition='Boolean om te bepalen of de markering machinaal of handmatig is aangebracht.',
                                        owner=self)

        self._isTijdelijk = OTLAttribuut(field=BooleanField,
                                         naam='isTijdelijk',
                                         label='is tijdelijk',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.isTijdelijk',
                                         definition='Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort.',
                                         owner=self)

        self._kleur = OTLAttribuut(field=KlKleurMarkering,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.kleur',
                                   definition='De kleur van de gebruikte markering.',
                                   owner=self)

        self._markeringsoort = OTLAttribuut(field=KlMarkeringSoort,
                                            naam='markeringsoort',
                                            label='markeringsoort',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsoort',
                                            definition='De soort van markering (verf, thermopast,...).',
                                            owner=self)

        self._markeringsysteemCopro = OTLAttribuut(field=DtcProductidentificatiecode,
                                                   naam='markeringsysteemCopro',
                                                   label='markeringsysteem COPRO',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.markeringsysteemCopro',
                                                   definition='De product informatie van de markering via COPRO codes.',
                                                   owner=self)

        self._opvatting = OTLAttribuut(field=DtcMarkeringOpvatting,
                                       naam='opvatting',
                                       label='opvatting',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering.opvatting',
                                       definition='De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur.',
                                       owner=self)

    @property
    def isHandwerk(self):
        """Boolean om te bepalen of de markering machinaal of handmatig is aangebracht."""
        return self._isHandwerk.get_waarde()

    @isHandwerk.setter
    def isHandwerk(self, value):
        self._isHandwerk.set_waarde(value, owner=self)

    @property
    def isTijdelijk(self):
        """Aanduiding of de wegmarkering al dan niet tot de werfsignalisatie behoort."""
        return self._isTijdelijk.get_waarde()

    @isTijdelijk.setter
    def isTijdelijk(self, value):
        self._isTijdelijk.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """De kleur van de gebruikte markering."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def markeringsoort(self):
        """De soort van markering (verf, thermopast,...)."""
        return self._markeringsoort.get_waarde()

    @markeringsoort.setter
    def markeringsoort(self, value):
        self._markeringsoort.set_waarde(value, owner=self)

    @property
    def markeringsysteemCopro(self):
        """De product informatie van de markering via COPRO codes."""
        return self._markeringsysteemCopro.get_waarde()

    @markeringsysteemCopro.setter
    def markeringsysteemCopro(self, value):
        self._markeringsysteemCopro.set_waarde(value, owner=self)

    @property
    def opvatting(self):
        """De opvatting van de markering, zijnde middelenverbintenis of resultaatsverbintenis met een minimale levensduur."""
        return self._opvatting.get_waarde()

    @opvatting.setter
    def opvatting(self, value):
        self._opvatting.set_waarde(value, owner=self)
