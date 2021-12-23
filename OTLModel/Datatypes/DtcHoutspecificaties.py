from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDuurzaamheidsklasseHout import KlDuurzaamheidsklasseHout
from OTLModel.Datatypes.KlKwaliteitsklasseHout import KlKwaliteitsklasseHout
from OTLModel.Datatypes.KlSterkteklasseHout import KlSterkteklasseHout


# Generated with OTLComplexDatatypeCreator
class DtcHoutspecificaties(ComplexField):
    """Complex datatype om de eigenschappen van hout te bundelen."""

    def __init__(self):
        super().__init__(naam="DtcHoutspecificaties",
                         label="Houtspecificaties",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties",
                         definition="Complex datatype om de eigenschappen van hout te bundelen.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.houtduurzaamheidsklasse = KeuzelijstField(naam="houtduurzaamheidsklasse",
                                                              label="houtduurzaamheidsklasse",
                                                              lijst=KlDuurzaamheidsklasseHout(),
                                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtduurzaamheidsklasse",
                                                              definition="De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden.",
                                                              constraints="",
                                                              usagenote="",
                                                              deprecated_version="")
        self.houtduurzaamheidsklasse = self.waarde.houtduurzaamheidsklasse
        """De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden."""

        self.waarde.houtkwaliteitsklasse = KeuzelijstField(naam="houtkwaliteitsklasse",
                                                           label="houtkwaliteitsklasse",
                                                           lijst=KlKwaliteitsklasseHout(),
                                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtkwaliteitsklasse",
                                                           definition="Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten.",
                                                           constraints="",
                                                           usagenote="",
                                                           deprecated_version="")
        self.houtkwaliteitsklasse = self.waarde.houtkwaliteitsklasse
        """Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten."""

        self.waarde.houtsterkteklasse = KeuzelijstField(naam="houtsterkteklasse",
                                                        label="houtsterkteklasse",
                                                        lijst=KlSterkteklasseHout(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtsterkteklasse",
                                                        definition="De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        self.houtsterkteklasse = self.waarde.houtsterkteklasse
        """De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is."""

        self.waarde.isResistentTegenMarieneBoorders = BooleanField(naam="isResistentTegenMarieneBoorders",
                                                                   label="is resistent tegen mariene boorders",
                                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.isResistentTegenMarieneBoorders",
                                                                   definition="Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water.",
                                                                   constraints="",
                                                                   usagenote="",
                                                                   deprecated_version="")
        self.isResistentTegenMarieneBoorders = self.waarde.isResistentTegenMarieneBoorders
        """Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water."""
