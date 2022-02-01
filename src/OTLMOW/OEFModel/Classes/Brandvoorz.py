# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Brandvoorz(EMObject):
    """Voorzieningen om branden te kunnen blussen, bv. brandhaspelkasten"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Brandvoorz'
    label = 'Brandvoorziening'

    def __init__(self):
        super().__init__()

