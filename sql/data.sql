DROP PROCEDURE IF EXISTS idb.insert_data;
DROP PROCEDURE IF EXISTS idb.get_data_in_realtime;
DROP PROCEDURE IF EXISTS idb.get_data_from;
DROP PROCEDURE IF EXISTS idb.get_data_from_to;
DROP PROCEDURE IF EXISTS idb.get_data;

DELIMITER $$

CREATE PROCEDURE idb.insert_data(label_id INTEGER, value FLOAT, updated DATETIME(6))
BEGIN
    INSERT INTO idb.data VALUES(label_id, value, updated);
END$$

CREATE PROCEDURE idb.get_data_in_realtime(graph_id INTEGER)
BEGIN
    SELECT label.device_id, label.id, data.value, data.updated
    FROM label, data, graph
    WHERE label.id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND graph_id=graph.id
        AND NOW(6) - INTERVAL graph.duration SECOND < data.updated
	ORDER BY data.updated ASC;
END$$

CREATE PROCEDURE idb.get_data_from(graph_id INTEGER)
BEGIN
    SELECT label.device_id, label.id, data.value, data.updated
    FROM label, data, graph
    WHERE label.id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND graph_id=graph.id
		AND graph.start < data.updated
	ORDER BY data.updated ASC;
END$$

CREATE PROCEDURE idb.get_data_from_to(graph_id INTEGER)
BEGIN
    SELECT label.device_id, label.id, data.value, data.updated
    FROM label, data, graph
    WHERE label.id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
        AND graph_id=graph.id
        AND graph.start < data.updated
        AND graph.finish > data.updated
	ORDER BY data.updated ASC;
END$$

CREATE PROCEDURE idb.get_data(graph_id INTEGER)
BEGIN
	SET @duration = (SELECT graph.duration FROM graph WHERE graph.id=graph_id);
    SET @start = (SELECT graph.start FROM graph WHERE graph.id=graph_id);
    SET @finish = (SELECT graph.finish FROM graph WHERE graph.id=graph_id);

	IF @duration IS NOT NULL THEN
		CALL get_data_in_realtime(graph_id);
	ELSEIF @start IS NOT NULL THEN
		IF @finish IS NOT NULL THEN
			CALL get_data_from_to(graph_id);
		ELSE
			CALL get_data_from(graph_id);
		END IF;
	END IF;
END$$

DELIMITER ;
