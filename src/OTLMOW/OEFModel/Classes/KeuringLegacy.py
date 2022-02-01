# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class KeuringLegacy(EMObject):
    """Specifiek opdrachttype : KEURING van de installatie"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#KeuringLegacy'
    label = 'Keuring (Legacy)'

    def __init__(self):
        super().__init__()

