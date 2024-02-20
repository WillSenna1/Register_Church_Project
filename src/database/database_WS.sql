"Criando DB"

CREATE DATABASE launch_WS;

USE  launch_WS;

CREATE TABLE member (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    birth INT NOT NULL,
    adress VARCHAR(200),
    phone VARCHAR(11),
    baptims VARCHAR(11),
    CONSTRAINT birth_check CHECK (birth > 0)
);


CREATE TABLE  event (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL
    );

    INSERT INTO event (title) VALUES 
    ('Consagração'),
    ('EBD'),
    ('Culto da Família'),
    ('Culto de Ensino'),
    ('Tarde da bênção'),
    ('Segunda de Primeira'),
    ('Vigília'),
    ('Ensaio')


CREATE TABLE presence (
    member_id INT NOT NULL,
    event_id INT NOT NULL,
    status ENUM('P', 'F') NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_member_id FOREIGN KEY (member_id) REFERENCES member(id),
    CONSTRAINT fk_event_id FOREIGN KEY (event_id) REFERENCES event(event_id),
    CHECK (date >= created_at)
);


