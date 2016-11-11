DROP PROCEDURE IF EXISTS idb.create_device;
DROP PROCEDURE IF EXISTS idb.change_device_name;
DROP PROCEDURE IF EXISTS idb.delete_device;

DROP PROCEDURE IF EXISTS idb.get_device_list;

DELIMITER $$

CREATE PROCEDURE idb.create_device()
BEGIN
    INSERT INTO device(name) VALUES('new device');
END$$

CREATE PROCEDURE idb.change_device_name(id INTEGER, name VARCHAR(255))
BEGIN
    UPDATE device SET device.name=name WHERE device.id=id;
END$$

CREATE PROCEDURE idb.delete_device(id INTEGER)
BEGIN
    DELETE FROM device WHERE device.id=id;
END$$

CREATE PROCEDURE idb.get_device_list()
BEGIN
    SELECT device.id, device.name, label.id, label.name
    FROM device LEFT JOIN label ON device.id=label.device_id
    ORDER BY device.id ASC, label.id ASC;
END$$

DELIMITER ;
