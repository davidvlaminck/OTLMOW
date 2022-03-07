import math
import warnings
from datetime import datetime

from OTLMOW.Facility.Exceptions.HasNoDotNotatieException import HasNoDotNotatieException
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.CachedProperty import cached_property
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField
from OTLMOW.OTLModel.Datatypes.UnionTypeField import UnionTypeField
from OTLMOW.OTLModel.Datatypes.UnionWaarden import UnionWaarden


class OTLAttribuut(AttributeInfo):
    def __init__(self, naam='', label='', objectUri='', definition='', constraints='', usagenote='', deprecated_version='',
                 kardinaliteit_min='1', kardinaliteit_max='1', field=OTLField, readonly=False, readonlyValue=None, owner=None):
        super().__init__()
        self.naam = naam
        self.label = label
        self.objectUri = objectUri
        self.definition = definition
        self.constraints = constraints
        self.usagenote = usagenote
        self.deprecated_version = deprecated_version
        self.readonly = readonly
        self.kardinaliteit_min = kardinaliteit_min
        self.kardinaliteit_max = kardinaliteit_max
        self._dotnotatie = ''
        self.owner = owner
        self.readonlyValue = None
        self.waarde = None
        self.field = field

        if readonly:
            self.__dict__["waarde"] = readonlyValue

        if self.field.waardeObject:
            self.waarde = self.field.waardeObject(parent=self)
            self.waarde._parent = self

        #if dotnotatie == '':
        #    self.add_dotnotatie()


    def default(self):
        if self.waarde is not dict and isinstance(self.waarde, list):
            valueList = []
            for item in self.waarde:
                if self.field.waardeObject is not None:
                    waardeDict = vars(item)
                    valueDict = {}
                    for k, v in waardeDict.items():
                        if v.default() is not None:
                            valueDict[k[1:]] = v.default()
                    if len(valueDict) != 0:
                        valueList.append(valueDict)
                else:
                    valueList.append(item)
            return valueList
        if self.field.waardeObject is not None:
            if self.field._uses_waarde_object:
                waardeDict = vars(self.waarde)
                valueDict = {}
                for k, v in waardeDict.items():
                    if v.default() is not None:
                        valueDict[k[1:]] = v.default()
                if len(valueDict) == 0:
                    return None
                return valueDict
            else:
                if self.waarde.waarde is not None:
                    if hasattr(self.waarde.waarde, 'default'):
                        return self.waarde.waarde.default()
                    else:
                        return self.waarde.waarde
                return None
        else:
            if isinstance(self.waarde, datetime):
                if self.waarde.hour == 0 and self.waarde.minute == 0 and self.waarde.second == 0:
                    return self.waarde.strftime("%Y-%m-%d")
                else:
                    return self.waarde.strftime("%Y-%m-%d %H:%M:%S")
            else:
                if hasattr(self.waarde, 'default'):
                    return self.waarde.default()
                else:
                    return self.waarde

    def set_waarde(self, value, owner=None):
        if owner is not None:
            if hasattr(owner, 'deprecated_version'):
                if owner.deprecated_version != '':
                    if hasattr(owner, 'typeURI'):
                        warnings.warn(message=f'{owner.typeURI} is deprecated since version {owner.deprecated_version}',
                                      category=DeprecationWarning)
                    else:
                        warnings.warn(message=f'used a class that is deprecated since version {owner.deprecated_version}',
                                      category=DeprecationWarning)

        if self.kardinaliteit_max == '*':
            kardinaliteit_max = math.inf
        else:
            kardinaliteit_max = int(self.kardinaliteit_max)
        if kardinaliteit_max > 1 and value is not None:
            kardinaliteit_min = int(self.kardinaliteit_min)
            if not isinstance(value, list):
                raise TypeError(f'expecting a list in {owner.__class__.__name__}.{self.naam}')
            elif isinstance(value, list) and isinstance(value, set):
                raise TypeError(f'expecting a non set type of list in {owner.__class__.__name__}.{self.naam}')
            elif 0 < len(value) < kardinaliteit_min:
                raise ValueError(f'expecting at least {kardinaliteit_min} element(s) in {owner.__class__.__name__}.{self.naam}')
            elif len(value) > kardinaliteit_max:
                raise ValueError(f'expecting at most {kardinaliteit_max} element(s) in {owner.__class__.__name__}.{self.naam}')
            for el_value in value:
                try:
                    field_validated = self.field.validate(self.field.convert_to_correct_type(el_value), self)
                    if not field_validated:
                        raise ValueError(
                            f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}')
                except TypeError as error:
                    raise ValueError(
                        f'invalid value in list for {owner.__class__.__name__}.{self.naam}: {el_value} is not valid, must be valid for {self.field.naam}\n' + str(
                            error))
            new_list = []
            for el_value in value:
                new_list.append(self.field.convert_to_correct_type(el_value))
            self.waarde = new_list
        else:
            if self.field.waardeObject is not None and isinstance(value, self.field.waardeObject):
                props = vars(self.field.waardeObject)
                for prop_key, prop_value in props.items():
                    if prop_key.startswith('_'):
                        continue
                    if prop_key != 'standaardEenheid':
                        a = getattr(value, prop_key)
                        setattr(self.waarde, prop_key, a)
            else:
                if self.field.validate(value=self.field.convert_to_correct_type(value), attribuut=self):
                    self.waarde = self.field.convert_to_correct_type(value)

        # check if kwant Ward inside a union type, if so, call clear_props
        if owner is not None and value is not None and hasattr(owner, 'field') and owner.field.waardeObject is not None and not owner.field._uses_waarde_object and not isinstance(owner.field, UnionTypeField) and owner.owner is not None and isinstance(owner.owner, UnionWaarden):
            owner.owner.clear_other_props('_' + owner.naam)


    def __str__(self):
        s = (f'information about {self.naam}:\n'
             f'naam: {self.naam}\n'
             f'uri: {self.objectUri}\n'
             f'definition: {self.definition}\n'
             f'label: {self.label}\n'
             f'usagenote: {self.usagenote}\n'
             f'constraints: {self.constraints}\n'
             f'readonly: {self.readonly}\n'
             f'kardinaliteit_min: {self.kardinaliteit_min}\n'
             f'kardinaliteit_max: {self.kardinaliteit_max}\n'
             f'deprecated_version: {self.deprecated_version}\n')
        return s

    @cached_property
    def dotnotatie(self):
        if self.field.waardeObject is not None:
            raise HasNoDotNotatieException(
                f"attribute {self.objectUri} does not have a dotnotatie because it has attributes itself.")

        if self._dotnotatie == '':
            self._dotnotatie = self.recurse_add_parents_to_dotnotatie(attribute=self)
        return self._dotnotatie

    @staticmethod
    def recurse_add_parents_to_dotnotatie(attribute):
        dotnotatie = attribute.naam
        if attribute.kardinaliteit_max == '*':
            kardinaliteit_max = math.inf
        else:
            kardinaliteit_max = int(attribute.kardinaliteit_max)
        if kardinaliteit_max > 1:
            dotnotatie += '[]'

        if attribute.owner is not None and hasattr(attribute.owner, '_parent') and attribute.owner._parent is not None and isinstance(
                attribute.owner._parent, OTLAttribuut):
            return attribute.recurse_add_parents_to_dotnotatie(attribute.owner._parent) + '.' + dotnotatie

        return dotnotatie

