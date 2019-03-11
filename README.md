# EIT_ET5

Projet d'analyse de texte en ET5

## Pour la partie LIMA

    SYNTAXE : python processing_lima_files.py [conll_file] [entity_ref_file] [tag_ref_file]

### Pour 04oct95

    python processing_lima_files.py 04oct95/formal-tst.NE.key.04oct95_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
    python evaluate.py output/output_tag.pos.lima output/output_tag.pos.ref

### Pour WSJ_0010

    python processing_lima_files.py wsj_0010/wsj_0010_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
    python evaluate.py output/output_ptb.pos.lima output/output_ptb.pos.ref
    python evaluate.py output/output_univ.pos.lima output/output_univ.pos.ref

## Pour la partie Stanford

### Partie 3

    Syntaxe : python TagConversion.py Path_To_POSTags_PTB_Universal_Linux.txt Path_To_Input.txt Path_to_output.txt
    Exemple : python TagConversion.py POSTags_PTB_Universal_Linux.txt wsj_0010_sample.txt.pos.stanford wsj_0010_sample.txt.pos.univ.stanford

### Partie 4

    Syntaxe: python NERFormat.py Path_To_Input.txt Path_to_output.txt
    Exemple: python NERFormat.py formal-tst.NE.key.04oct95_small.txt.output new-format.NE.key.04oct95_small.txt

### Partie 5

#### FormatEspace.py

    Syntaxe: python FormatEspace.py Path_To_Input.txt Path_to_output.txt

#### FormatRefToLima.py

    Syntax: python FormatRefToLima.py Path_To_Input.txt Path_to_output.txt
    Example: python FormatRefToLima.py formal-tst.NE.key.04oct95_small.ne output.04oct95.ne.lima

#### LimaToStanford.py

    Syntaxe: python LimaToStanford.py Path_To_POSTags_LIMA_Stanford.txt Path_To_Input.txt Path_to_output.txt

#### ToEvaluateFormat.py

    Syntaxe: python toEvaluateFormat.py Path_To_Input.txt Path_to_output.txt