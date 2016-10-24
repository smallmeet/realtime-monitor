DROP PROCEDURE IF EXISTS idb.create_graph;
DROP PROCEDURE IF EXISTS idb.change_graph_name;
DROP PROCEDURE IF EXISTS idb.delete_graph;
DROP PROCEDURE IF EXISTS idb.toggle_graph;

DELIMITER $$

CREATE PROCEDURE idb.create_graph()
BEGIN
    INSERT INTO graph(`name`) VALUES('new graph');
END$$

CREATE PROCEDURE idb.change_graph_name(id INTEGER, name VARCHAR(255))
BEGIN
    UPDATE graph SET graph.name=name WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.delete_graph(id INTEGER)
BEGIN
    DELETE FROM graph WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.toggle_graph(id INTEGER)
BEGIN
    UPDATE graph SET graph.duration=IF(graph.activated=1, NULL, 20) WHERE graph.id=id;
    UPDATE graph SET graph.activated=IF(graph.activated=1, 0, 1) WHERE graph.id=id;
END$$

DELIMITER ;
