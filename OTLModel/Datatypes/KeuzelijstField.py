from OTLModel.BaseClasses.OTLField import OTLField


class KeuzelijstField(OTLField):
    options = {}
    codelist = ''

    @staticmethod
    def validate(value, attribuut):
        if not isinstance(value, str):
            raise TypeError(f'{value} is not the correct type. Expecting a string')
        if value is not None and not value in attribuut.field.options.keys():
            raise ValueError(
                f'{value} is not a valid option for {attribuut.naam}, find the valid options using .attr_type_info("{attribuut.naam}")')
        return True

    def __str__(self):
        s = f"""information about {self.naam}:
naam: {self.naam}
uri: {self.objectUri}
definition: {self.definition}
label: {self.label}
usagenote: {self.usagenote}
deprecated_version: {self.deprecated_version}"""
        s += '\npossible values:\n'
        s += '\n'.join(list(map(lambda x: '    ' + x.invulwaarde, self.options.values())))
        return s
