# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class GebUitr(EMObject):
    """Gebouwuitrusting : verlichting, stopcontacten, verwarming, koeling, ..."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#GebUitr'
    label = 'Gebouwuitrusting'

    def __init__(self):
        super().__init__()

