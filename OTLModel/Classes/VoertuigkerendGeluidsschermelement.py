# coding=utf-8
from OTLModel.Classes.BijlageVoertuigkering import BijlageVoertuigkering
from OTLModel.Classes.Geluidsschermelement import Geluidsschermelement
from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.EigenschappenVoertuigkering import EigenschappenVoertuigkering
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACWerkingsbreedte import KlLEACWerkingsbreedte


# Generated with OTLClassCreator. To modify: extend, do not edit
class VoertuigkerendGeluidsschermelement(BijlageVoertuigkering, Geluidsschermelement, SchokindexVoertuigkering, EigenschappenVoertuigkering):
    """Dit zijn schermelementen met een voet in de vorm van een T. Op de voet worden deltablocs geplaatst die een stabiliserende en voertuigkerende functie hebben."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BijlageVoertuigkering.__init__(self)
        EigenschappenVoertuigkering.__init__(self)
        Geluidsschermelement.__init__(self)
        SchokindexVoertuigkering.__init__(self)

        self.werkingsbreedte = KeuzelijstField(naam="werkingsbreedte",
                                               label="werkingsbreedte",
                                               lijst=KlLEACWerkingsbreedte(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoertuigkerendGeluidsschermelement.werkingsbreedte",
                                               definition="Dit is de afstand, op het voorvlak van een schermelement en loodrecht op de as van de weg gemeten, tussen de voorkant van het schermelement in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van het schermelement bij aanrijding.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """Dit is de afstand, op het voorvlak van een schermelement en loodrecht op de as van de weg gemeten, tussen de voorkant van het schermelement in normale positie en de plaats van het verst uitwijkend onderdeel aan de achterzijde van het schermelement bij aanrijding."""
