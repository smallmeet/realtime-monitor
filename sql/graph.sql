DROP PROCEDURE IF EXISTS idb.create_graph;
DROP PROCEDURE IF EXISTS idb.change_graph_name;
DROP PROCEDURE IF EXISTS idb.delete_graph;

DROP PROCEDURE IF EXISTS idb.toggle_graph;
DROP PROCEDURE IF EXISTS idb.change_ordering;

DROP PROCEDURE IF EXISTS idb.set_interval;

DROP PROCEDURE IF EXISTS idb.attach_label;
DROP PROCEDURE IF EXISTS idb.detach_label;

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
    SET @order = (SELECT graph.ordering FROM graph WHERE graph.id=id);
    DELETE FROM graph WHERE graph.id=id;
    UPDATE graph SET graph.ordering=IF(graph.activated=1, graph.ordering-1, graph.ordering) WHERE graph.ordering > @order;
END$$

CREATE PROCEDURE idb.toggle_graph(id INTEGER)
BEGIN
    SET @order = (SELECT graph.ordering FROM graph WHERE graph.id=id);
    SET @is_active = (SELECT graph.activated FROM graph WHERE graph.id=id);
    SET @max = (SELECT MAX(graph.ordering)+1 FROM graph);
    UPDATE graph SET graph.ordering=IF(@is_active=1, -1, @max) WHERE graph.id=id;
    UPDATE graph SET graph.ordering=IF(@is_active=1, graph.ordering-1, graph.ordering) WHERE graph.ordering > @order;
    UPDATE graph SET graph.activated=IF(@is_active=1, 0, 1) WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.change_ordering(id INTEGER, ordering INTEGER)
BEGIN
    SET @origin = (SELECT graph.ordering FROM graph WHERE graph.id=id);
    IF @origin < ordering THEN
        UPDATE graph SET graph.ordering=graph.ordering-1 WHERE @origin < graph.ordering AND graph.ordering <= ordering;
        UPDATE graph SET graph.ordering=ordering WHERE graph.id=id;
    ELSEIF @origin > ordering THEN
        UPDATE graph SET graph.ordering=graph.ordering+1 WHERE ordering <= graph.ordering AND graph.ordering < @origin;
        UPDATE graph SET graph.ordering=ordering WHERE graph.id=id;
    END IF;
END$$

CREATE PROCEDURE idb.set_interval(id INTEGER, duration INTEGER, start DATETIME(6), finish DATETIME(6), data_count INTEGER)
BEGIN
    UPDATE graph SET graph.duration=duration WHERE graph.id=id;
    UPDATE graph SET graph.start=start WHERE graph.id=id;
    UPDATE graph SET graph.finish=finish WHERE graph.id=id;
    UPDATE graph SET graph.data_count=data_count WHERE graph.id=id;
END$$

CREATE PROCEDURE idb.attach_label(graph_id INTEGER, label_id INTEGER)
BEGIN
    INSERT INTO connects VALUES(graph_id, label_id);
END$$

CREATE PROCEDURE idb.detach_label(graph_id INTEGER, label_id INTEGER)
BEGIN
    DELETE FROM connects WHERE connects.graph_id=graph_id AND connects.label_id=label_id;
END$$

DELIMITER ;
