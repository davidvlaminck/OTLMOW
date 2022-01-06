# coding=utf-8
from OTLModel.Classes.Bebakening import Bebakening
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWegbebakeningType import KlWegbebakeningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class WegbebakeningAfschermendeConstructies(Bebakening):
    """Een houder met reflector op een constructie met als doel het verkeer te geleiden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWegbebakeningType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WegbebakeningAfschermendeConstructies.type",
                                    definition="De vorm van wegbebakening voor afschermende constructies.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De vorm van wegbebakening voor afschermende constructies."""
