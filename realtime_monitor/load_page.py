def getDeviceList(conn):
    cur = conn.cursor()
    devices = []
    cur.execute('CALL get_device_list()')
    for row in cur:
        if len(devices) == 0 or devices[-1][0] != int(row[0]):
            devices.append([int(row[0]), row[1], []])
        if row[2] is not None:
            devices[-1][2].append([int(row[2]), row[3]])
    cur.close()
    return devices

def getGraphList(conn):
    cur = conn.cursor()
    graphs = []
    cur.execute('CALL get_graph_list()')
    for row in cur:
        if len(graphs) == 0 or graphs[-1][0] != int(row[0]):
            graphs.append([int(row[0]), row[1], row[2], []])
        if row[3] is not None:
            graphs[-1][3].append([int(row[3]), row[4]])
    cur.close()
    return graphs
