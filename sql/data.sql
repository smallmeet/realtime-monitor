DROP PROCEDURE IF EXISTS idb.insert_data;
DROP PROCEDURE IF EXISTS idb.get_data;

DELIMITER $$

CREATE PROCEDURE idb.insert_data(label_id INTEGER, value FLOAT, updated DATETIME(6))
BEGIN
    INSERT INTO idb.data VALUES(label_id, value, updated);
END$$

CREATE PROCEDURE idb.get_data(graph_id INTEGER)
BEGIN
    SELECT label.id, data.value, data.updated
    FROM label, data, graph
    WHERE label.id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND graph_id=graph.id
        AND (graph.duration IS NULL OR NOW(6) - INTERVAL graph.duration SECOND < data.updated)
        AND (graph.start IS NULL OR graph.start < data.updated)
        AND (graph.finish IS NULL OR graph.finish > data.updated)
    ORDER BY data.updated ASC;
END$$

DELIMITER ;
