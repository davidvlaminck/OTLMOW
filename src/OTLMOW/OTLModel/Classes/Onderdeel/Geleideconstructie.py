# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AansluitendeConstructie import AansluitendeConstructie
from OTLMOW.OTLModel.Classes.Abstracten.EigenschappenVoertuigkering import EigenschappenVoertuigkering
from OTLMOW.OTLModel.Classes.Abstracten.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleideconstructie(AansluitendeConstructie, EigenschappenVoertuigkering, SchokindexVoertuigkering):
    """Een doorlopende afschermende constructie voor voertuigen geïnstalleerd langs de weg of in de middenberm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AansluitendeConstructie.__init__(self)
        EigenschappenVoertuigkering.__init__(self)
        SchokindexVoertuigkering.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SluitAanOp', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Eindstuk')

        self._isVerwijderbaar = OTLAttribuut(field=BooleanField,
                                             naam='isVerwijderbaar',
                                             label='is verwijderbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.isVerwijderbaar',
                                             definition='Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden.',
                                             owner=self)

        self._werkingsbreedte = OTLAttribuut(field=KlLEACWerkingsbreedte,
                                             naam='werkingsbreedte',
                                             label='werkingsbreedte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.werkingsbreedte',
                                             definition='Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding.',
                                             owner=self)

    @property
    def isVerwijderbaar(self):
        """Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden."""
        return self._isVerwijderbaar.get_waarde()

    @isVerwijderbaar.setter
    def isVerwijderbaar(self, value):
        self._isVerwijderbaar.set_waarde(value, owner=self)

    @property
    def werkingsbreedte(self):
        """Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding."""
        return self._werkingsbreedte.get_waarde()

    @werkingsbreedte.setter
    def werkingsbreedte(self, value):
        self._werkingsbreedte.set_waarde(value, owner=self)
