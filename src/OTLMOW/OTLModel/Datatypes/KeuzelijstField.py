import warnings

from OTLMOW.Facility.Exceptions.RemovedOptionError import RemovedOptionError
from OTLMOW.OTLModel.BaseClasses.OTLField import OTLField


class KeuzelijstField(OTLField):
    options = {}
    codelist = ''

    @staticmethod
    def validate(value, attribuut):
        if value is not None:
            if not isinstance(value, str):
                raise TypeError(f'{value} is not the correct type. Expecting a string')
            if not value in attribuut.field.options.keys():
                raise ValueError(
                    f'{value} is not a valid option for {attribuut.naam}, find the valid options using .attr_type_info("{attribuut.naam}")')

            option_value = attribuut.field.options[value]
            if option_value.status == 'uitgebruik':
                warnings.warn(message=f'{value} is a deprecated value for {attribuut.naam}, please refrain from using this value.',
                              category=DeprecationWarning)
            if option_value.status == 'verwijderd':
                raise RemovedOptionError(f'{value} is not a valid value for {attribuut.naam}. This will result in a valdation '
                                         'error when updating this attribute.')
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
