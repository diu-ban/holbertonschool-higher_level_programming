-- 6-states.sql
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states FROM hbtn_0d_usa (
    id INT DEFAULT 1 NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY(id)
);