DROP SCHEMA IF EXISTS VirologyDatabase;
CREATE DATABASE VirologyDatabase;
USE VirologyDatabase;

CREATE TABLE genome (
  genome_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  molecule_type VARCHAR(10) NOT NULL,
  descript VARCHAR(50) NOT NULL,
  PRIMARY KEY  (genome_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE gene (
  gene_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  genome_id SMALLINT UNSIGNED NOT NULL,
  nt_seq VARCHAR(650) NOT NULL,
  descript VARCHAR(50) NOT NULL,
  PRIMARY KEY  (gene_id),
  FOREIGN KEY (genome_id) REFERENCES genome (genome_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE taxonomy (
  taxonomy_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
  family VARCHAR(50) NOT NULL,
  order_v VARCHAR(50) NOT NULL,
  class VARCHAR(50) NOT NULL,
  phylum VARCHAR(50) NOT NULL,
  kingdom VARCHAR(50) NOT NULL,
  realm VARCHAR(50) NOT NULL,
  PRIMARY KEY  (taxonomy_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE virus (
	virus_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name_v VARCHAR(100) NOT NULL,
    genome_id SMALLINT UNSIGNED NOT NULL,
    taxonomy_id SMALLINT UNSIGNED NOT NULL,
    virus_type VARCHAR(50) NOT NULL,
    shape VARCHAR(30) NOT NULL,
    year_origin INT DEFAULT NULL,
    PRIMARY KEY (virus_id),
    KEY (name_v),
    FOREIGN KEY (genome_id) REFERENCES genome (genome_id),
    FOREIGN KEY (taxonomy_id) REFERENCES taxonomy (taxonomy_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE db_query (
	query_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	query_seq VARCHAR(650) NOT NULL,
	query_name VARCHAR(100) NOT NULL,
	query_message VARCHAR(50) NOT NULL,
    PRIMARY KEY (query_id),
    KEY (query_seq),
    KEY (query_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE hitSeq (
	hit_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	query_seq VARCHAR(650) NOT NULL,
	hit_index FLOAT NOT NULL,
	hit_seq VARCHAR(650) NOT NULL,
	name_v VARCHAR(100) NOT NULL,
	gene_id SMALLINT UNSIGNED NOT NULL,
    PRIMARY KEY (hit_id),
    FOREIGN KEY (query_seq) REFERENCES db_query (query_seq),
    FOREIGN KEY (name_v) REFERENCES virus (name_v),
    FOREIGN KEY (gene_id) REFERENCES gene (gene_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE hitName (
	hit_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    query_name VARCHAR(100) NOT NULL,
    virus_id SMALLINT UNSIGNED NOT NULL,
	PRIMARY KEY (hit_id),
    FOREIGN KEY (query_name) REFERENCES db_query (query_name),
    FOREIGN KEY (virus_id) REFERENCES virus (virus_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE genome ADD INDEX index_molecule_type (molecule_type);
ALTER TABLE taxonomy ADD INDEX index_family (family);
ALTER TABLE taxonomy ADD INDEX index_class (class);
ALTER TABLE taxonomy ADD INDEX index_realm (realm);
ALTER TABLE virus ADD INDEX index_shape (shape);
ALTER TABLE virus ADD INDEX index_year_origin (year_origin);