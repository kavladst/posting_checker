CREATE SCHEMA IF NOT EXISTS posts;

CREATE TABLE IF NOT EXISTS posts.phrase_region (
    id uuid PRIMARY KEY,
    phrase TEXT NOT NULL,
    region TEXT NOT NULL,
    updated_at timestamp with time zone NOT NULL ,
    UNIQUE (phrase, region)
);

CREATE TABLE IF NOT EXISTS posts.count_records (
    id uuid PRIMARY KEY,
    phrase_region_id uuid NOT NULL,
    count INT NOT NULL,
    created_at timestamp with time zone NOT NULL,
    FOREIGN KEY (phrase_region_id) REFERENCES posts.phrase_region (id) ON DELETE CASCADE
);

CREATE INDEX phrase_region_id_index ON posts.count_records (phrase_region_id);
