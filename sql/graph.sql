DROP PROCEDURE IF EXISTS idb.create_graph;
DROP PROCEDURE IF EXISTS idb.change_graph_name;
DROP PROCEDURE IF EXISTS idb.delete_graph;
DROP PROCEDURE IF EXISTS idb.toggle_graph;
DROP PROCEDURE IF EXISTS idb.set_duration;
DROP PROCEDURE IF EXISTS idb.set_start_and_finish;

DELIMITER $$

CREATE PROCEDURE idb.create_graph()
BEGIN
    INSERT INTO graph(name, activated, ordering, duration) VALUES('new graph', 0, -1, 20);
END$$

CREATE PROCEDURE idb.change_graph_name(id INTEGER, name VARCHAR(255))
BEGIN
    UPDATE graph SET graph.name=name WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.delete_graph(id INTEGER)
BEGIN
    SELECT @graphOrder:=graph.ordering FROM graph WHERE graph.id=id;
    DELETE FROM graph WHERE graph.id=id;
    UPDATE graph SET graph.ordering=IF(graph.activated=1, graph.ordering-1, graph.ordering) WHERE graph.ordering > @graphOrder;
END$$

CREATE PROCEDURE idb.toggle_graph(id INTEGER)
BEGIN
    SELECT @graphOrder:=graph.ordering FROM graph WHERE graph.id=id;
    SELECT @activation:=graph.activated FROM graph WHERE graph.id=id;
    SELECT @max:=MAX(ordering)+1 FROM graph;
    UPDATE graph SET graph.ordering=IF(@activation=1, -1, @max) WHERE graph.id=id;
    UPDATE graph SET graph.ordering=IF(@activation=1, graph.ordering-1, graph.ordering) WHERE graph.ordering > @graphOrder;
    UPDATE graph SET graph.activated=IF(@activation=1, 0, 1) WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.set_duration(id INTEGER, duration INTEGER)
BEGIN
    UPDATE graph SET graph.duration=duration WHERE graph.id=id;
    UPDATE graph SET graph.start=NULL WHERE graph.id=id;
    UPDATE graph SET graph.finish=NULL WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.set_start_and_finish(id INTEGER, start DATETIME(6), finish DATETIME(6))
BEGIN
    UPDATE graph SET graph.duration=NULL WHERE graph.id=id;
    UPDATE graph SET graph.start=start WHERE graph.id=id;
    UPDATE graph SET graph.finish=finish WHERE graph.id=id;
END$$

DELIMITER ;
