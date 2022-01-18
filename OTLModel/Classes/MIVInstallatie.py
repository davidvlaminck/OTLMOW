# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.NaampadObject import NaampadObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVInstallatie(NaampadObject, AttributeInfo):
    """De volledige opstelling voor meten in Vlaanderen op een bepaalde locatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        NaampadObject.__init__(self)

        self._lusConfig = OTLAttribuut(field=DtcDocument,
                                       naam='lusConfig',
                                       label='lus config',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.lusConfig',
                                       usagenote='Bestanden van het type xlsx.',
                                       definition='Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie.')

        self._technischeDocumentatie = OTLAttribuut(field=DtcDocument,
                                                    naam='technischeDocumentatie',
                                                    label='technische documentatie',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#MIVInstallatie.technischeDocumentatie',
                                                    usagenote='Bestanden van het type pdf.',
                                                    definition='Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator,  ...')

    @property
    def lusConfig(self):
        """Een definierende tabel die relatie legt tussen meetpuntnummer lusvolgorde nummer en de GPS locatie."""
        return self._lusConfig.waarde

    @lusConfig.setter
    def lusConfig(self, value):
        self._lusConfig.set_waarde(value, owner=self)

    @property
    def technischeDocumentatie(self):
        """Documentatie van de onderdelen: LVE / luskaart / communicatiekaart, configurator,  ..."""
        return self._technischeDocumentatie.waarde

    @technischeDocumentatie.setter
    def technischeDocumentatie(self, value):
        self._technischeDocumentatie.set_waarde(value, owner=self)
