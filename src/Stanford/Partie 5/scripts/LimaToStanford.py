# FEURTE - GONCALVES - VOLLMER
# Polytech 2018

'''
	Syntax: python LimaToStanford.py Path_To_POSTags_LIMA_Stanford.txt Path_To_Input.txt Path_to_output.txt
	Example: 
'''

import sys
import os

if __name__=="__main__":
	args = sys.argv
	if len(args) != 4:
		print("Syntax : python LimaToStanford.py Path_To_POSTags_LIMA_Stanford.txt Path_To_Input.txt Path_to_output.txt")
		sys.exit(1)

	tags_filename = args[1]
	input_filename = args[2]
	output_filename = args[3]

	with open(tags_filename, "r") as tags_file:
		dictLIMAtoStanford = {}
		for line in tags_file:
			split_line = line.split()
			dictLIMAtoStanford[split_line[0]] = split_line[1]

	with open(input_filename, "r") as input_file:
		output = ""
		lines = input_file.readlines()
		lines = [i.strip() for i in lines]
		for line in lines:
			split_line = line.split(" ")
			for token in split_line:
				word = token.split("_")

				if len(word) > 0:
					if word[1] in dictLIMAtoStanford.keys():
						tag = dictLIMAtoStanford[word[1]]
						output += word[0] + "_" + tag + " "
				else:
					output += word[0] + " "

		with open(output_filename, "w") as output_file:
			output_file.write(output)