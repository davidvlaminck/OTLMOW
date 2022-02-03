# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject
from OTLMOW.OEFModel.EMAttribuut import EMAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField


# Generated with OEFClassCreator. To modify: extend, do not edit
class ANPRPaal(EMObject):
    """ANPRPAAL"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#ANPRPaal'
    label = 'ANPR paal'

    def __init__(self):
        super().__init__()

        self._galgpaal = EMAttribuut(field=BooleanField,
                                     naam='Galgpaal',
                                     label='Galgpaal',
                                     objectUri='https://lgc.data.wegenenverkeer.be/ns/attribuut#ANPRPaal.galgpaal',
                                     definitie='Is de asset een galgpaal?',
                                     owner=self)

    @property
    def galgpaal(self):
        """Is de asset een galgpaal?"""
        return self._galgpaal.waarde

    @galgpaal.setter
    def galgpaal(self, value):
        self._galgpaal.set_waarde(value, owner=self)

