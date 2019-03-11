# FEURTE - GONCALVES - VOLLMER
# Polytech 2018

'''
	Syntax: python NERFormat.py Path_To_Input.txt Path_to_output.txt
	Example: python NERFormat.py formal-tst.NE.key.04oct95_small.txt.output new-format.NE.key.04oct95_small.txt
'''

import sys
import os

if __name__=="__main__":
	args = sys.argv
	if len(args) != 3:
		print("Syntax : python FormatNER.py Path_To_Input.txt Path_to_output.txt")
		sys.exit(1)

	input_filename = args[1]
	output_filename = args[2]

	with open(input_filename, "r") as input_file:
		ne_word = {}
		ne_type = {}
		occurrences = 0	
			
		lines = input_file.readlines()
		lines = [i.strip() for i in lines]
		for line in lines:
			split_line = line.split(" ")
			for token in split_line:
				word = token.split("/")
				if word[1] == "PERSON" or word[1] == "ORGANIZATION" or word[1] == "LOCATION":
					occurrences = occurrences + 1
					if word[0] not in ne_word:
						ne_type[word[0]] = word[1]
						ne_word[word[0]] = 1
					else:
						ne_word[word[0]] = ne_word[word[0]] + 1

		with open(output_filename, "w+") as output_file:
			for k, v in ne_type.items():
				output_file.write(k + "\t" + v + "\t" + str(ne_word[k]) + "\t" 
									+ str(((float(ne_word[k]) / occurrences) * 100)) + "\t" 
									+ "(" + str(ne_word[k]) + "/" + str(occurrences) + ")\n")
