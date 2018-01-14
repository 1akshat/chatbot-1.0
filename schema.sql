drop table if exists chat;
    create table chat (
    id integer primary key autoincrement,
    query VARCHAR(100),
    response VARCHAR(100),
    dated TIMESTAMP
);