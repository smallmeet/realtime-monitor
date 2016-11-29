DROP PROCEDURE IF EXISTS idb.insert_data;
DROP PROCEDURE IF EXISTS idb.get_data;

DELIMITER $$

CREATE PROCEDURE idb.insert_data(label_id INTEGER, value FLOAT, updated DATETIME(6))
BEGIN
    INSERT INTO idb.data VALUES(label_id, value, updated);
END$$

CREATE PROCEDURE idb.get_data(graph_id INTEGER)
BEGIN
    SET @data_count = (SELECT graph.data_count FROM graph WHERE graph.id=graph_id);
    set @graph_id = graph_id;
    IF @data_count IS NULL THEN
        SELECT data.label_id, data.value, data.updated
        FROM data, graph
        WHERE data.label_id IN (SELECT label_id FROM connects WHERE connects.graph_id=graph_id)
            AND graph.id=graph_id
            AND (graph.duration IS NULL OR NOW(6) - INTERVAL graph.duration SECOND < data.updated)
            AND (graph.start IS NULL OR graph.start < data.updated)
            AND (graph.finish IS NULL OR graph.finish > data.updated)
        ORDER BY data.updated ASC;
    ELSE
        SET @query = '
        SELECT * FROM (
            SELECT data.label_id, data.value, data.updated
            FROM data, graph
            WHERE data.label_id IN (SELECT label_id FROM connects WHERE connects.graph_id=?)
                AND graph.id=?
            ORDER BY data.updated DESC LIMIT ?
        ) AS alias
        ORDER BY alias.updated ASC;';
        PREPARE STMT from @query;
        EXECUTE STMT USING @graph_id, @graph_id, @data_count;
    END IF;
END$$

DELIMITER ;
