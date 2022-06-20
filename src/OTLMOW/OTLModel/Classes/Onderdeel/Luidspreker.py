# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KLLuidsprekerVormgeving import KLLuidsprekerVormgeving
from OTLMOW.OTLModel.Datatypes.KlAudioTransportType import KlAudioTransportType
from OTLMOW.OTLModel.Datatypes.KlLuidsprekerMerk import KlLuidsprekerMerk
from OTLMOW.OTLModel.Datatypes.KlLuidsprekerModelnaam import KlLuidsprekerModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Luidspreker(AIMNaamObject, PuntGeometrie):
    """Een luidspreker is een apparaat waarmee elektrische signalen worden omgezet in geluid."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlLuidsprekerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.merk',
                                  definition='Het merk van de luidspreker.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlLuidsprekerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.modelnaam',
                                       definition='De modelnaam van de luidspreker.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.technischeFiche',
                                             definition='De technische fiche van de luidspreker.',
                                             owner=self)

        self._transportType = OTLAttribuut(field=KlAudioTransportType,
                                           naam='transportType',
                                           label='transport type',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.transportType',
                                           definition='Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel.',
                                           owner=self)

        self._vormgeving = OTLAttribuut(field=KLLuidsprekerVormgeving,
                                        naam='vormgeving',
                                        label='vormgeving',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Luidspreker.vormgeving',
                                        definition='Soort luidsprekers volgens zijn vormfactor.',
                                        owner=self)

    @property
    def merk(self):
        """Het merk van de luidspreker."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de luidspreker."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de luidspreker."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def transportType(self):
        """Geeft aan op welke manier het audiosignaal wordt getransporteerd door het toestel."""
        return self._transportType.get_waarde()

    @transportType.setter
    def transportType(self, value):
        self._transportType.set_waarde(value, owner=self)

    @property
    def vormgeving(self):
        """Soort luidsprekers volgens zijn vormfactor."""
        return self._vormgeving.get_waarde()

    @vormgeving.setter
    def vormgeving(self, value):
        self._vormgeving.set_waarde(value, owner=self)
