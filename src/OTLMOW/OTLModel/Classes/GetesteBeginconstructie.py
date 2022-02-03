# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLMOW.OTLModel.Classes.Beginstuk import Beginstuk
from OTLMOW.OTLModel.Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class GetesteBeginconstructie(SchokindexVoertuigkering, Beginstuk):
    """Een gecertificeerd begin aan een geleideconstructie,met als doel de ernst van een frontale botsing te reduceren aan de stroomopwaartse zijde ten opzichte van de meest nabij gelegen rijstrook."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Beginstuk.__init__(self)
        SchokindexVoertuigkering.__init__(self)

        self._performantieklasse = OTLAttribuut(field=KlLEACPerformantieklasse,
                                                naam='performantieklasse',
                                                label='performantieklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#GetesteBeginconstructie.performantieklasse',
                                                definition='De aanduiding hoe (performantie) de beginconstructie is getest.',
                                                owner=self)

    @property
    def performantieklasse(self):
        """De aanduiding hoe (performantie) de beginconstructie is getest."""
        return self._performantieklasse.waarde

    @performantieklasse.setter
    def performantieklasse(self, value):
        self._performantieklasse.set_waarde(value, owner=self)
