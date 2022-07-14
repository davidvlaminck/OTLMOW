import random

from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.Facility.Exceptions.UnionTypeError import UnionTypeError


class UnionTypeField(OTLField):
    def __str__(self):
        return OTLField.__str__(self)

    waarde_shortcut_applicable = False

    @staticmethod
    def validate(value, attribuut):
        if value is None:
            return True
        if type(value) == attribuut.field.waardeObject:
            return True
        valueDict = vars(attribuut.field.waardeObject())
        for val_in_dict in valueDict.values():
            if val_in_dict is None:
                continue
            try:
                validate_result = val_in_dict.field.validate(value, val_in_dict)
                if validate_result:
                    return True
            except:
                raise UnionTypeError(
                    f'Invalid value for {attribuut.naam}, check attr_type_info to see what kind of values are valid.')
        raise UnionTypeError(f'Invalid value for {attribuut.naam}, check attr_type_info to see what kind of values are valid.')

    @classmethod
    def create_dummy_data(cls):
        if cls.waardeObject is None:
            raise NotImplementedError
        valid_attrs = []
        new_value_object = cls.waardeObject()
        for attr in dir(new_value_object):
            if attr.startswith('__') or not attr.startswith('_') or attr == '_parent':
                continue
            valid_attrs.append(getattr(new_value_object, attr))

        selected_attr = random.choice(valid_attrs)
        selected_attr.set_waarde(selected_attr.field.create_dummy_data())
        return new_value_object


