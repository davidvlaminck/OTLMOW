# coding=utf-8
from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.EigenschappenVoertuigkering import EigenschappenVoertuigkering
from OTLModel.Classes.AansluitendeConstructie import AansluitendeConstructie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class Geleideconstructie(SchokindexVoertuigkering, EigenschappenVoertuigkering, AansluitendeConstructie):
    """Een doorlopende afschermende constructie voor voertuigen geïnstalleerd langs de weg of in de middenberm."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        SchokindexVoertuigkering.__init__(self)
        EigenschappenVoertuigkering.__init__(self)
        AansluitendeConstructie.__init__(self)

        self.isVerwijderbaar = BooleanField(naam="isVerwijderbaar",
                                            label="is verwijderbaar",
                                            objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.isVerwijderbaar",
                                            definition="Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Geleideconstructie kan met minimale moeite tijdelijk worden weggenomen en teruggeplaatst worden."""

        self.werkingsbreedte = KeuzelijstField(naam="werkingsbreedte",
                                               label="werkingsbreedte",
                                               lijst=KlLEACWerkingsbreedte(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Geleideconstructie.werkingsbreedte",
                                               definition="Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Op het voorvlak van een geleideconstructie en loodrecht op de as van de weg gemeten afstand tussen de voorkant van de geleideconstructie in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van de geleideconstructie bij aanrijding."""
