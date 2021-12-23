from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.TerreinDeel import TerreinDeel
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWegbermBIO import KlWegbermBIO
from OTLModel.Datatypes.KlWegbermType import KlWegbermType


# Generated with OTLClassCreator
class Wegberm(AIMObject, TerreinDeel):
    """Gedeelte van het wegplatform dat buiten de rijbanen ligt. Een wegberm kan sloten en bijzonder ingerichte onderdelen bevatten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        TerreinDeel.__init__(self)
        self.bijzonderIngerichteOnderdelen = KeuzelijstField(naam="bijzonderIngerichteOnderdelen",
                                                             label="bijzonder ingerichte onderdelen van de wegberm",
                                                             lijst=KlWegbermBIO(),
                                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.bijzonderIngerichteOnderdelen",
                                                             definition="De bijzonder ingerichte onderdelen van de wegberm.",
                                                             constraints="",
                                                             usagenote="",
                                                             deprecated_version="")
        """De bijzonder ingerichte onderdelen van de wegberm."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlWegbermType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wegberm.type",
                                    definition="Het type van wegberm.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type van wegberm."""
