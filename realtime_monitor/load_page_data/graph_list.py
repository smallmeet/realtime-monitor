def getGraphList(conn):
    cur = conn.cursor()
    graphes = []
    cur.execute('CALL get_graph_list()')
    for row in cur:
        if len(graphes) == 0 or graphes[-1][0] != int(row[0]):
            graphes.append([int(row[0]), row[1], row[2], []])
        if row[3] is not None:
            graphes[-1][3].append([int(row[3]), row[4]])
    cur.close()
    return graphes
