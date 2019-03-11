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
	
	
Commandes pour le III :

III.1.d
dans EIT_ET5/src/coreNLP/stanford-postagger-2018-10-16 :
./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt > sample-input.txt.pos

III.2.a
dans EIT_ET5/src/coreNLP/stanford-postagger-2018-10-16 :
./stanford-postagger.sh models/english-left3words-distsim.tagger ../wsj_0010_sample.txt > ../wsj_0010_sample.txt.pos.stanford

III.2.b

dans EIT_ET5/src/coreNLP/stanford-postagger-2018-10-16 :
python3 evaluate.py wsj_0010_sample.txt.pos.stanford wsj_0010_sentence.pos.ref
Warning: the reference and the candidate consists of different number of lines!
Word precision: 0.7464788732394366
Word recall: 0.4818181818181818
Tag precision: 0.7323943661971831
Tag recall: 0.4727272727272727
Word F-measure: 0.5856353591160222
Tag F-measure: 0.574585635359116

III.2.c
python3 evaluate.py wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.txt.pos.univ.ref



python3 PTBtoUniv.py ../POSTags_PTB_Universal_Linux.txt ../wsj_0010_sample.txt.pos.stanford ../texts/wsj_0010_sample.txt.pos.univ.stanford
