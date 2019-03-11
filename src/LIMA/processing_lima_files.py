# FEURTE - GONCALVES - VOLLMER
# Polytech 2018


# SYNTAX : python processing_lima_files.py [conll_file] [entity_ref_file] [tag_ref_file]
# Pour 04oct95 :
# 	python processing_lima_files.py 04oct95/formal-tst.NE.key.04oct95_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
# 	python evaluate.py output/output_tag.pos.lima output/output_tag.pos.ref
#
# Pour WSJ_0010 :
#	python processing_lima_files.py wsj_0010/wsj_0010_sample.txt.conll 04oct95/formal-tst.NE.key.04oct95_sample.ne wsj_0010/wsj_0010_sample.txt.pos.ref
#	python evaluate.py output/output_ptb.pos.lima output/output_ptb.pos.ref
#	python evaluate.py output/output_univ.pos.lima output/output_univ.pos.ref


import os
import re
import sys
import glob
from lxml import etree as eee

tag_file = "POSTags_PTB_Universal.txt"

def parseConllFile(c_file, ptb):
	with open(c_file) as f:
	    content = f.readlines()
	content = [x.strip() for x in content]
	specific_entities = []

	for line in content:
		if(line != ""):
			split_line = line.split("\t")
			#print(split_line)
			token_name = split_line[1]
			token_id = split_line[4]
			token_type = split_line[5]

			specific_entities.append((token_name, token_id, token_type))

	msyn_token, tag = "", ""
	for line in specific_entities:
		# for word in line[0].split(" "):
		# 	msyn_token += (word + "_" + (line[1] if ptb else PTB_to_Universal(line[1])) + " ")
		msyn_token += (multipleWordToken(line[0]) + "_" + (line[1] if ptb else PTB_to_Universal(line[1])) + " ") # TODO : check
		tag += getTagFromLine(line)

	return msyn_token, tag

def parseEntityRefFile(ref_file):
	with open(ref_file) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	
	entity = ""
	for line in content:
		results = re.findall(r"<ENAMEX TYPE=\"(PERSON|ORGANIZATION|LOCATION)\">(.*?)</ENAMEX>", line, re.DOTALL)
		for result in results:
			entity += multipleWordToken(result[1]) + "_" + result[0] + " "

	return entity


def parseTagRefFile(ref_file):
	with open(ref_file) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	
	ptb_tag = "" 
	univ_tag = ""

	for line in content:
		split_line = line.split(" ")
		for wordAndTag in split_line:
			word = wordAndTag.split("_")[0]
			tag = wordAndTag.split("_")[1]

			ptb_tag += wordAndTag + " "
			univ_tag += word + "_" + PTB_to_Universal(tag) + " "

	return ptb_tag, univ_tag


def saveOutputInFile(output, filename):
	with open(filename, "w") as f:
		f.write(output)
	
	return
	
def PTB_to_Universal(tag):
	with open(tag_file) as f:
	    content = f.readlines()
	content = [x.strip() for x in content]
	ret = "None"
	
	for line in content:
		words = line.split(" ")
		if(words[0] == tag):
			ret = words[1]
			break
	
	return ret
	
	
def multipleWordToken(token):
	split_token = token.split(" ")
	if(len(split_token)):
		token = "Espace".join(split_token)
		
	return token

def removeEspaceToken(output):
	words = output.split()
	for word in words:
		if("Espace" in word):
			new_word = word.replace("Espace", " ")
			print(new_word)
			output = output.replace(word, new_word)
	return output

def getTagFromLine(line):
	if(line[2] != "_"):
		tag = line[2].split(".")[1]
		if(tag == "LOCATION" or tag == "ORGANIZATION" or tag == "PERSON"):
			return (multipleWordToken(line[0]) + "_" + line[2].split(".")[1] + " ")

	return ""


if __name__=="__main__":
	# Parsing args 
	args = sys.argv
	if len(args) != 3 and len(args) != 4:
		print("Syntax : python processing_lima_files.py [file.conll] [entity_ref_file] [tag_ref_file]")
		sys.exit(1)
	conll_file = args[1]
	entity_ref_file = args[2]
	tag_ref_file = args[3] if len(args) == 4 else ""

	if not os.path.exists(conll_file):
		print("Conll file %s does not exist." % conll_file)
		sys.exit(1)
	if not os.path.exists(entity_ref_file):
		print("Entity ref file %s does not exist." % entity_ref_file)
		sys.exit(1)

	# Parse conllFile to PTB and Universal
	output_ptb, output_entity = parseConllFile(conll_file, True)
	output_ptb = removeEspaceToken(output_ptb)
	output_entity = removeEspaceToken(output_entity)
	output_universal, output_entity = parseConllFile(conll_file, False)
	output_universal = removeEspaceToken(output_universal)
	output_entity = removeEspaceToken(output_entity)
	
	# Save the output in files
	print("Parsing the conll file \"%s\" to output_ptb.pos.lima, output_univ.pos.lima and output_entity.pos.lima !" % conll_file)
	saveOutputInFile(output_ptb, "output/output_ptb.pos.lima")
	saveOutputInFile(output_universal, "output/output_univ.pos.lima")
	saveOutputInFile(output_entity, "output/output_entity.pos.lima")

	# Parse the entity ref file
	print("Parsing the entity ref file \"%s\" to output_entity.pos.ref" % entity_ref_file)
	output_entity_ref = parseEntityRefFile(entity_ref_file)
	output_entity_ref = removeEspaceToken(output_entity_ref)
	saveOutputInFile(output_entity_ref, "output/output_entity.pos.ref")

	if not os.path.exists(tag_ref_file):
		if(os.path.isfile("output/output_ptb.pos.ref")):
			os.remove("output/output_ptb.pos.ref")
		if(os.path.isfile("output/output_univ.pos.ref")):
			os.remove("output/output_univ.pos.ref")
		if(tag_ref_file != ""):
			print("Tag ref file %s does not exist." % tag_ref_file)
			sys.exit(1)
	else:
		# Parse the morpho-syntaxic tag ref file
		print("Parsing the morpho-syntaxic tag ref file \"%s\" to output_ptb.pos.ref and output_univ.pos.ref !" % tag_ref_file)
		output_ptb_ref, output_univ_ref = parseTagRefFile(tag_ref_file)
		saveOutputInFile(output_ptb_ref, "output/output_ptb.pos.ref")
		saveOutputInFile(output_univ_ref, "output/output_univ.pos.ref")

	