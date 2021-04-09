DROP SCHEMA IF EXISTS VirologyDatabase;
CREATE DATABASE VirologyDatabase;
USE VirologyDatabase;

CREATE TABLE genome (
  genome_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  molecule_type VARCHAR(50) NOT NULL,
  descript VARCHAR(500) NOT NULL,
  PRIMARY KEY  (genome_id)
);

CREATE TABLE gene (
  gene_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  genome_id SMALLINT UNSIGNED NOT NULL,
  nt_seq VARCHAR(15000) NOT NULL,
  descript VARCHAR(500) NOT NULL,
  PRIMARY KEY  (gene_id),
  FOREIGN KEY (genome_id) REFERENCES genome (genome_id)
);

CREATE TABLE taxonomy (
  taxonomy_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  family VARCHAR(100) NOT NULL,
  order_v VARCHAR(100) NOT NULL,
  class VARCHAR(100) NOT NULL,
  phylum VARCHAR(100) NOT NULL,
  kingdom VARCHAR(100) NOT NULL,
  realm VARCHAR(100) NOT NULL,
  PRIMARY KEY  (taxonomy_id)
);

CREATE TABLE virus (
	virus_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name_v VARCHAR(100) NOT NULL,
    genome_id SMALLINT UNSIGNED NOT NULL,
    taxonomy_id SMALLINT UNSIGNED NOT NULL,
    virus_type VARCHAR(100) NOT NULL,
    shape VARCHAR(100) NOT NULL,
    year_origin INT DEFAULT NULL,
    PRIMARY KEY (virus_id),
    KEY (name_v),
    FOREIGN KEY (genome_id) REFERENCES genome (genome_id),
    FOREIGN KEY (taxonomy_id) REFERENCES taxonomy (taxonomy_id)
);
CREATE TABLE db_query (
	query_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	query_seq VARCHAR(768) NOT NULL,
	query_name VARCHAR(100) NOT NULL,
	query_message VARCHAR(15000) NOT NULL,
    PRIMARY KEY (query_id),
    KEY (query_seq),
    KEY (query_name)
);

CREATE TABLE hitSeq (
	hit_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	query_seq VARCHAR(768) NOT NULL,
	hit_index FLOAT NOT NULL,
	hit_seq VARCHAR(15000) NOT NULL,
	name_v VARCHAR(100) NOT NULL,
	gene_id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (hit_id),
    FOREIGN KEY (query_seq) REFERENCES db_query (query_seq),
    FOREIGN KEY (name_v) REFERENCES virus (name_v),
    FOREIGN KEY (gene_id) REFERENCES gene (gene_id)
); 

CREATE TABLE hitName (
	hit_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    query_name VARCHAR(100) NOT NULL,
    virus_id SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (hit_id),
    FOREIGN KEY (query_name) REFERENCES db_query (query_name),
    FOREIGN KEY (virus_id) REFERENCES virus (virus_id)
);

SELECT * FROM genome;

SELECT * FROM gene;

SELECT * FROM taxonomy;

SELECT * FROM virus;

SELECT * FROM db_query;

SELECT * FROM hitSeq;

SELECT * FROM hitName;