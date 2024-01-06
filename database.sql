CREATE TABLE User (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

CREATE TABLE Post (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES User(id)
);

INSERT INTO User (username, email) VALUES ('john_doe', 'john@example.com');

