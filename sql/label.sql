DROP PROCEDURE IF EXISTS idb.create_label;
DROP PROCEDURE IF EXISTS idb.change_label_name;
DROP PROCEDURE IF EXISTS idb.delete_label;

DELIMITER $$

CREATE PROCEDURE idb.create_label(device_id INTEGER)
BEGIN
    INSERT INTO label(`name`) VALUES('new label');
    INSERT INTO includes VALUES(device_id, LAST_INSERT_ID());
END$$

CREATE PROCEDURE idb.change_label_name(id INTEGER, name VARCHAR(255))
BEGIN
    UPDATE label SET label.name=name WHERE label.id=id;
END$$

CREATE PROCEDURE idb.delete_label(id INTEGER)
BEGIN
    DELETE FROM label WHERE label.id=id;
END$$

DELIMITER ;
