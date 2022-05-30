class WKTValidator:
    @classmethod
    def validate_wkt(cls, input_string: str) -> bool:
        if not '(' in input_string or not ')' in input_string:
            return False
        geo_type = input_string.split(' (')[0]

        # TODO add multi
        if geo_type not in ('POINT', 'POINT Z', 'LINESTRING', 'LINESTRING Z', 'POLYGON', 'POLYGON Z'):
            return False

        if geo_type.startswith('POLYGON'):
            punten = input_string.split(' ((')[1]
            if punten[-2:] != '))':
                return False
            punten = punten[:-2]
            if '), (' in input_string:
                polygons = punten.split('), (')
                for polygon in polygons:
                    puntenlijst = polygon.split(', ')
                    validated = WKTValidator.validate_puntenlijst(geo_type, puntenlijst)
                    if not validated:
                        return False
                return True
            else:
                if ', ' in punten:
                    puntenlijst = punten.split(', ')
                else:
                    puntenlijst = punten.split(',')
                return WKTValidator.validate_puntenlijst(geo_type, puntenlijst)
        else:
            punten = input_string.split(' (')[1]
            if punten[-1] != ')':
                return False
            punten = punten[:-1]
            puntenlijst = punten.split(', ')
            return WKTValidator.validate_puntenlijst(geo_type, puntenlijst)

    @classmethod
    def validate_puntenlijst(cls, geo_type, puntenlijst):
        if geo_type.startswith('POINT') and len(puntenlijst) != 1:
            return False
        if geo_type.startswith('LINESTRING') and len(puntenlijst) < 2:
            return False
        if geo_type.startswith('POLYGON') and len(puntenlijst) < 3:
            return False

        for punt in puntenlijst:
            coords = punt.split(' ')
            if geo_type.endswith(' Z') and len(coords) != 3:
                return False
            if not geo_type.endswith(' Z') and len(coords) != 2:
                return False

            for coord in coords:
                try:
                    val = float(coord)
                    if val < 0:
                        return False
                except Exception:
                    return False

        return True