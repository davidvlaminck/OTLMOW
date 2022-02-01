# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class WIM(EMObject):
    """Weigh-In-Motion installatie (meet en detecteert rijdende vrachtwagens die overladen zijn)"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#WIM'
    label = 'Weigh-In-Motion'

    def __init__(self):
        super().__init__()

