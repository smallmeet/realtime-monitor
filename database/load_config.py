def loadConfig(filename):
    fp = open(filename, 'r')
    result = ''
    for line in fp:
        result += line.strip()
    return eval(result)
