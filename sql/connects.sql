DROP PROCEDURE IF EXISTS idb.attach_label;
DROP PROCEDURE IF EXISTS idb.detach_label;

DELIMITER $$

CREATE PROCEDURE idb.attach_label(graph_id INTEGER, label_id INTEGER)
BEGIN
    INSERT INTO connects VALUES(graph_id, label_id);
END$$

CREATE PROCEDURE idb.detach_label(graph_id INTEGER, label_id INTEGER)
BEGIN
    DELETE FROM connects WHERE connects.graph_id=graph_id AND connects.label_id=label_id;
END$$

DELIMITER ;
