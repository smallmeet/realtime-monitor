DROP PROCEDURE IF EXISTS idb.insert_data;
DROP PROCEDURE IF EXISTS idb.get_data_in_realtime;
DROP PROCEDURE IF EXISTS idb.get_data_from;
DROP PROCEDURE IF EXISTS idb.get_data_from_to;

DELIMITER $$

CREATE PROCEDURE idb.insert_data(label_id INTEGER, value FLOAT, updated DATETIME(6))
BEGIN
    INSERT INTO idb.data VALUES(label_id, value, updated);
END$$

CREATE PROCEDURE idb.get_data_in_realtime(graph_id INTEGER, duration INTEGER)
BEGIN
    SELECT pair.device_id, pair.label_id, pair.value, pair.updated
    FROM (
        SELECT includes.device_id, data.label_id, data.value, data.updated
        FROM includes, data
        WHERE includes.label_id=data.label_id
    ) AS pair, connects
    WHERE pair.label_id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND NOW(6) - INTERVAL duration SECOND < pair.updated;
END$$

CREATE PROCEDURE idb.get_data_from(graph_id INTEGER, `from` DATETIME(6))
BEGIN
    SELECT pair.device_id, pair.label_id, pair.value, pair.updated
    FROM (
        SELECT includes.device_id, data.label_id, data.value, data.updated
        FROM includes, data
        WHERE includes.label_id=data.label_id
    ) AS pair, connects
    WHERE pair.label_id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND `from` < pair.updated;
END$$

CREATE PROCEDURE idb.get_data_from_to(graph_id INTEGER, `from` DATETIME(6), `to` DATETIME(6))
BEGIN
    SELECT pair.device_id, pair.label_id, pair.value, pair.updated
    FROM (
        SELECT includes.device_id, data.label_id, data.value, data.updated
        FROM includes, data
        WHERE includes.label_id=data.label_id
    ) AS pair, connects
    WHERE pair.label_id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND `from` < pair.updated
        AND `to` > pair.updated;
END$$

DELIMITER ;
