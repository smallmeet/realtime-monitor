DROP DATABASE IF EXISTS idb;

CREATE DATABASE idb;

CREATE TABLE idb.device (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE idb.label (
    device_id INTEGER NOT NULL,
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    FOREIGN KEY (device_id) REFERENCES device(id) ON DELETE CASCADE
);

CREATE TABLE idb.graph (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    activated INTEGER NOT NULL,
    ordering INTEGER NOT NULL,
    duration INTEGER,
    start DATETIME(6),
    finish DATETIME(6),
    data_count INTEGER
);

CREATE TABLE idb.data (
    label_id INTEGER NOT NULL,
    value FLOAT NOT NULL,
    updated DATETIME(6) NOT NULL,
    FOREIGN KEY (label_id) REFERENCES label(id) ON DELETE CASCADE
);

CREATE TABLE idb.connects (
    graph_id INTEGER NOT NULL,
    label_id INTEGER NOT NULL,
    FOREIGN KEY (graph_id) REFERENCES graph(id) ON DELETE CASCADE,
    FOREIGN KEY (label_id) REFERENCES label(id) ON DELETE CASCADE
);
