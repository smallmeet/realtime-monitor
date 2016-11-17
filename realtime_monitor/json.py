def dict2json(d):
    return str(d).replace('\'', '\"')

def json2dict(j):
    return eval(j)

def loadJSON(lines):
    result = ''
    for line in lines:
        result += line.strip()

    return json2dict(result)
