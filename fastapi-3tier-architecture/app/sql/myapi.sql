CREATE SCHEMA IF NOT EXISTS myapi;

CREATE TABLE IF NOT EXISTS myapi.movies (
  movie_id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  released INTEGER NOT NULL,
  rating NUMERIC(2, 1) NOT NULL
);

CREATE TABLE IF NOT EXISTS myapi.users (
    user_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    hashed_password TEXT NOT NULL,
    UNIQUE(email)
);