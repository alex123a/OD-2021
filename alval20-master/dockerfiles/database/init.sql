CREATE DATABASE myDatabase;
USE myDatabase;

CREATE TABLE persons(
    PersonID int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    Firstname VARCHAR(150) NOT NULL,
    Lastname VARCHAR(150) NOT NULL
);

INSERT INTO persons(Firstname, Lastname) VALUES("Mads", "Jensen");
INSERT INTO persons(Firstname, Lastname) VALUES("Mathias", "Neerup");