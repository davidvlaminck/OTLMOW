class UnionTypeField:
    def __init__(self, *args):
        self.fieldList = []
        for arg in args:
            self.fieldList.append(arg)

    def __get__(self, instance, owner):
        try:
            return instance.__dict__[self.name]
        except KeyError:
            return None

    def __set__(self, instance, value):
        if not self.check_if_field_in_list(value):
            raise TypeError(f'expecting correct type in {self.name}. Correct types are of type {self.fieldList}')
        instance.__dict__[self.name] = value

    def check_if_field_in_list(self, value):
        for field in self.fieldList:
            if isinstance(value, field):
                return True
        return False

    def __set_name__(self, owner, name):
        self.name = name
