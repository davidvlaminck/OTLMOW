def wrap_in_quotes(input: str) -> str:
    if not isinstance(input, str):
        raise TypeError
    if input == '':
        return "''"
    singles = sum(1 for c in input if c == "'")
    doubles = sum(1 for c in input if c == '"')
    if singles > doubles:
        if doubles > 0:
            return '"' + input.replace('"', '\\"') + '"'
        return '"' + input + '"'
    else:
        if singles > 0:
            return "'" + input.replace("'", "\\'") + "'"
        return "'" + input + "'"
