class MeerKardinaliteitField:
    def __init__(self, fieldType):
        self._type = fieldType
        self.list = []

    def __get__(self, instance, owner):
        return self.list

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'expecting list in {self.name}')
        badtype = self.check_types_in_list(value)
        if badtype:
            raise ValueError(f'element of bad type in {self.name}')

        self.list = value

    def check_types_in_list(self, valueList):
        badtype = False
        for el in valueList:
            if not (isinstance(el, self._type)):
                badtype = True
                return badtype
        return badtype

    def __set_name__(self, owner, name):
        self.name = name

        # aanpassen naar eigen list implementatie
        # waarbij kardinaliteit en type kan gecheckt worden bij set
        # testen met 2 overervende klasses van field met dezelfde naam (andere instantie)
        # https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#ContainerBuis.kleur
        # kard 1 *
        # De kleur van de coating.
