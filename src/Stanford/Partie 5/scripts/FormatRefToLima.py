# FEURTE - GONCALVES - VOLLMER
# Polytech 2018

'''
	Syntax: python FormatRefToLima.py Path_To_Input.txt Path_to_output.txt
	Example: python FormatRefToLima.py formal-tst.NE.key.04oct95_small.ne output.04oct95.ne.lima
'''

import sys
import os
import re

if __name__=="__main__":
	args = sys.argv
	if len(args) != 3:
		print("Syntax : python FormatRefToLima.py Path_To_Input.txt Path_to_output.txt")
		sys.exit(1)

	input_filename = args[1]
	output_filename = args[2]

	with open(input_filename, "r") as input_file:
		lines = input_file.readlines()
		lines = [i.strip() for i in lines]
		output = ""
		for line in lines:			
			find = re.findall(r"<ENAMEX TYPE=\"(PERSON|ORGANIZATION|LOCATION)\">(.*?)</ENAMEX>", line, re.DOTALL)
			for token in find:
				split_token = token[1].split(" ")
				if(len(split_token)):
					output += "Espace".join(split_token) + "_" + token[0] + " "
				else:
					output += token[1] + "_" + token[0] + " "

		with open(output_filename, "w") as output_file:
			output_file.write(output)