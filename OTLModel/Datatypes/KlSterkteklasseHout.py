from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlSterkteklasseHout(Keuzelijst):
    """De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning."""

    def __init__(self):
        super().__init__(naam="KlSterkteklasseHout",
                         label="Sterkteklasse van hout",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlSterkteklasseHout",
                         definition="De klasse die de maximale belasting van het hout aangeeft. Gebruik letter C voor naaldhout en D voor loofhout, gevolgd door een getal dat betrekking heeft op de karakteristieke buigspanning.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSterkteklasseHout")

