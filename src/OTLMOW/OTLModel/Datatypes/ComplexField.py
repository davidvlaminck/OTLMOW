﻿from abc import ABC
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class ComplexField(OTLField, ABC):
    def __str__(self):
        return OTLField.__str__(self)

    waarde_shortcut_applicable = False
