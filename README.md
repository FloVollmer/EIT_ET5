# EIT_ET5
Projet d'analyse de texte en ET5


# Pour la partie LIMA :

    SYNTAXE : python processing_lima_files.py [conll_file] [entity_ref_file] [tag_ref_file]
    
## Pour 04oct95 :
 	python processing_lima_files.py 04oct95/formal-tst.NE.key.04oct95_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
 	python evaluate.py output/output_tag.pos.lima output/output_tag.pos.ref

## Pour WSJ_0010 :
    python processing_lima_files.py wsj_0010/wsj_0010_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
    python evaluate.py output/output_ptb.pos.lima output/output_ptb.pos.ref
    python evaluate.py output/output_univ.pos.lima output/output_univ.pos.ref
