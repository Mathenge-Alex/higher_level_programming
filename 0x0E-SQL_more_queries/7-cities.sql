-- Creates database hbtn_0d_usa and table cities (database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id)
	REFERENCES hbtn_0d_usa.states(id)
);
