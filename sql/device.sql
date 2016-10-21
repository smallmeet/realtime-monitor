DROP PROCEDURE IF EXISTS idb.create_device;
DROP PROCEDURE IF EXISTS idb.delete_device;

DELIMITER $$

CREATE PROCEDURE idb.create_device()
BEGIN
    INSERT INTO device(`name`) VALUES('new device');
END$$

CREATE PROCEDURE idb.delete_device(id INTEGER)
BEGIN
    DELETE FROM device WHERE device.id=id;
END$$

DELIMITER ;
