from realtime_monitor.validation import check_number

def isValid(data):
    data = data.split('/')
    if len(data)%2 != 0:
        return False
    for i in range(0, len(data), 2):
        if not data[i].isdigit() or not check_number.isFloat(data[i+1]):
            return False

    return True
