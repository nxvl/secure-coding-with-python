DROP TABLE IF EXISTS listings;

CREATE TABLE listings(
    id   SERIAL                 NOT NULL,
    title VARCHAR(128)          NOT NULL,
    description VARCHAR(500)    NOT NULL,
    PRIMARY KEY (id)
);