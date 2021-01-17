DROP TABLE IF EXISTS games CASCADE;
DROP TABLE IF EXISTS ratings CASCADE;
DROP TABLE IF EXISTS earnings CASCADE;

CREATE TABLE IF NOT EXISTS games (
  id serial PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  platform VARCHAR(255),
  publisher VARCHAR(255),
  release_date DATE,
  genre VARCHAR(255),
  game_engine VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS ratings (
  id serial PRIMARY KEY,
  game_id INTEGER,
  metacritic INTEGER,
  TS_rating DECIMAL(4,2),
  rank_type VARCHAR(255),
  ranking INTEGER,
  date_created DATE,
  CONSTRAINT fk_game
    FOREIGN KEY (game_id)
    REFERENCES games (id)
);


CREATE TABLE IF NOT EXISTS earnings (
  id serial PRIMARY KEY,
  game_id INTEGER,
  price DECIMAL NOT NULL,
  inapp BOOLEAN NOT NULL,
  shows_ads BOOLEAN NOT NULL,
  revenue BIGINT,
  downloads BIGINT,
  CONSTRAINT fk_game
    FOREIGN KEY (game_id)
    REFERENCES games (id)
);



