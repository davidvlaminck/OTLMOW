from abc import abstractmethod


class OTLField:
    waarde_shortcut_applicable = False
    naam = ''
    label = ''
    objectUri = ''
    definition = ''
    usagenote = ''
    deprecated_version = ''
    waardeObject = None

    @staticmethod
    def validate(value, attribuut):
        if attribuut.field.waardeObject:
            if not isinstance(value, attribuut.field.waardeObject):
                raise ValueError(
                    f'This is a complex datatype. Set the values through the attributes. Use .attr_type_info() for more info')
            validation = True
            for attr_key, attr in vars(value).items():
                if attr_key == '_parent':
                    continue
                if attr.waarde is None:
                    continue
                if attr.kardinaliteit_max != '1':
                    for value_item in attr.waarde:
                        if not attr.field.validate(value_item, attr):
                            validation = False
                            break
                else:
                    if not attr.field.validate(attr.waarde, attr):
                        validation = False
                        break
            return validation
        pass

    @staticmethod
    def value_default(value):
        return value

    @staticmethod
    def convert_to_correct_type(value) -> object:
        return value

    @abstractmethod
    def __str__(self):
        return f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""
