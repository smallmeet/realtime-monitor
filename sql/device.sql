DROP PROCEDURE IF EXISTS idb.create_device;
DROP PROCEDURE IF EXISTS idb.delete_device;

DELIMITER $$

CREATE PROCEDURE idb.create_device()
BEGIN
    INSERT INTO device(`name`) VALUES('new device');
END$$

CREATE PROCEDURE idb.delete_device(id INTEGER)
BEGIN
    DELETE FROM data WHERE data.label_id IN (
        SELECT label.id FROM label, includes WHERE includes.device_id=id AND includes.label_id=label.id
    );
    DELETE FROM connects WHERE connects.label_id IN (
        SELECT label.id FROM label, includes WHERE includes.device_id=id AND includes.label_id=label.id
    );
    DELETE FROM label WHERE label.id IN (
        SELECT label_id FROM includes WHERE includes.device_id=id
    );
    DELETE FROM device WHERE device.id=id;
END$$

DELIMITER ;
