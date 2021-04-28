SELECT * FROM virus WHERE shape = "Helical";
SELECT virus_id, name_v, year_origin FROM virus WHERE year_origin >= 2010 ORDER BY year_origin;
SELECT * FROM hitSeq WHERE length(name_v) >= 30;
SELECT virus_id, name_v, virus_type FROM virus WHERE INSTR(virus_type,"DNA") > 0 ORDER BY virus_type;
SELECT * FROM gene WHERE INSTR(nt_seq,"AGCUCAUG") > 0;
SELECT * FROM taxonomy WHERE class="Megaviricetes";

SELECT g.gene_id, g.genome_id, g.nt_seq, G.molecule_type FROM gene g JOIN genome G WHERE g.genome_id = G.genome_id;
SELECT v.virus_id, v.name_v, t.family, t.order_v, t.class, t.phylum, t.kingdom, t.realm FROM virus v JOIN taxonomy t WHERE v.taxonomy_id = t.taxonomy_id ORDER BY realm;
SELECT v.virus_id, v.name_v, v.virus_type, g.molecule_type FROM virus v JOIN genome g WHERE v.genome_id = g.genome_id AND v.virus_id%2=0;
SELECT hs.hit_id, hs.name_v, hs.hit_index, hs.query_seq, db.query_seq FROM hitSeq hs JOIN db_query db WHERE hs.query_seq=db.query_seq;
SELECT v.name_v, g.molecule_type, v.virus_type, v.shape FROM virus v JOIN genome g WHERE INSTR(v.virus_type,"DNA") > 0 AND g.genome_id = v.genome_id;
SELECT hn.query_name, hn.virus_id, v.virus_type, v.shape FROM hitName hn JOIN virus v WHERE hn.virus_id=v.virus_id;

SELECT * FROM virus WHERE taxonomy_id IN (SELECT taxonomy_id FROM taxonomy WHERE realm="Riboviria"); 
SELECT * FROM gene WHERE genome_id IN (SELECT genome_id FROM genome WHERE molecule_type="RNA");
SELECT * FROM hitSeq WHERE gene_id IN (SELECT gene_id FROM gene WHERE length(nt_seq) >= 430 AND length(nt_seq) <= 460);
SELECT * FROM taxonomy WHERE taxonomy_id = (SELECT t.taxonomy_id FROM taxonomy t JOIN virus v WHERE t.taxonomy_id = v.taxonomy_id AND v.name_v="Dengue virus");
SELECT * FROM genome WHERE genome_id IN (SELECT v.genome_id FROM virus v JOIN genome g WHERE g.genome_id=v.genome_id AND v.shape="Helical") ORDER BY genome_id;
SELECT * FROM genome WHERE genome_id IN (SELECT G.genome_id FROM genome G JOIN gene g WHERE G.genome_id = g.genome_id AND INSTR(g.nt_seq,"AGCUCAUG") > 0);

SELECT genome_id, COUNT(*) "Total Genes" FROM gene WHERE genome_id%2=1 GROUP BY genome_id;
SELECT v.virus_id, v.name_v, v.virus_type, v.shape, v.year_origin, t.family FROM virus v JOIN 
(SELECT taxonomy_id, family FROM taxonomy WHERE family="Podoviridae") AS t ON v.taxonomy_id = t.taxonomy_id ORDER BY v.virus_id;