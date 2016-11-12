DROP PROCEDURE IF EXISTS idb.get_device_list;
DROP PROCEDURE IF EXISTS idb.get_graph_list;

DELIMITER $$

CREATE PROCEDURE idb.get_device_list()
BEGIN
    SELECT device.id, device.name, label.id, label.name
    FROM device LEFT JOIN label ON device.id=label.device_id
    ORDER BY device.id ASC, label.id ASC;
END$$

CREATE PROCEDURE idb.get_graph_list()
BEGIN
    SELECT graph.id, graph.name, graph.activated, label.id, label.name
    FROM graph
        LEFT JOIN connects ON graph.id=connects.graph_id
        LEFT JOIN label ON connects.label_id=label.id
    ORDER BY graph.activated=1 DESC, graph.ordering ASC, graph.id ASC, label.id ASC;
END$$

DELIMITER ;
