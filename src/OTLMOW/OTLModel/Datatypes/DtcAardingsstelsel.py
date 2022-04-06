# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlAardingAardingsstelsel import KlAardingAardingsstelsel


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAardingsstelselWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._attestDNB = OTLAttribuut(field=DtcDocument,
                                       naam='attestDNB',
                                       label='attest distributienetbeheerder',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel.attestDNB',
                                       usagenote='Voor een globaal aardingsstelsel moet een attest voorzien worden zoniet moet er van uitgegaan worden dat het om een gescheiden stelsel gaat ',
                                       definition='Een bestandsbijlage met het attest volgens het aardingsstelsel voorzien door de distributienetbeheerder .',
                                       owner=self)

        self._type = OTLAttribuut(field=KlAardingAardingsstelsel,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel.type',
                                  definition='Geeft het type aan van het aardingsstelsel volgens een keuzelijst.',
                                  owner=self)

    @property
    def attestDNB(self):
        """Een bestandsbijlage met het attest volgens het aardingsstelsel voorzien door de distributienetbeheerder ."""
        return self._attestDNB.waarde

    @attestDNB.setter
    def attestDNB(self, value):
        self._attestDNB.set_waarde(value, owner=self._parent)

    @property
    def type(self):
        """Geeft het type aan van het aardingsstelsel volgens een keuzelijst."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcAardingsstelsel(ComplexField, AttributeInfo):
    """Complex datatype dat het mogelijk maakt om het attest van de distributienetbeheerder toe te voegen in het geval van een globaal aardingsstelsel."""
    naam = 'DtcAardingsstelsel'
    label = 'Aardingsstelsel details.'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#DtcAardingsstelsel'
    definition = 'Complex datatype dat het mogelijk maakt om het attest van de distributienetbeheerder toe te voegen in het geval van een globaal aardingsstelsel.'
    usagenote = 'Het attest is enkel vereist voor globale aardingsstelsels. Voor gescheiden aardinsstelsel kanhet attribuut attestDNB leeg blijven.'
    waardeObject = DtcAardingsstelselWaarden

    def __str__(self):
        return ComplexField.__str__(self)

