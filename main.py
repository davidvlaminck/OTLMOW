import sqlite3


class OSLOClass:
    def __init__(self):
        pass

    def __init__(self, label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version):
        self.label_nl = label_nl
        self.name = name
        self.uri = uri
        self.definition_nl = definition_nl
        self.usagenote_nl = usagenote_nl
        self.abstract = abstract
        self.deprecated_version = deprecated_version


def readSQlite():
    con = sqlite3.connect('InputFiles/OTL.db')
    cur = con.cursor()

    for row in cur.execute("SELECT label_nl, name, uri, definition_nl, usagenote_nl, abstract, deprecated_version FROM OSLOClass where uri=:uriclass", {"uriclass": 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AansluitendeConstructie'}):
        print(row)
        c = OSLOClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        print(c)

    con.close()


if __name__ == '__main__':
    readSQlite()
