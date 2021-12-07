from OTLClasses.Verification.AIMNaamObject import AIMNaamObject


class Aftakking(AIMNaamObject):
    """Groep van stroomkringen specifiek bedoeld voor de aansturing van wegverlichting.In het typeschema autosnelwegen worden
    er standaard 4 aftakkingen voorzien: middenberm (hoofdrijbaan),op- en afritten + signalisatie,gewestweg,parking. """

    def __init__(self):
        self.loadGeldigeRelaties()  # TODO move to Factory?

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking"
