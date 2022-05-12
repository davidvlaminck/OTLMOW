from abc import ABC
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class ComplexField(OTLField, ABC):
    def __str__(self):
        return OTLField.__str__(self)

    _uses_waarde_object = True
