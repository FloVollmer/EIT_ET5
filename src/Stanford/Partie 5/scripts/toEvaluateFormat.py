# FEURTE - GONCALVES - VOLLMER
# Polytech 2018

'''
	Syntax: python toEvaluateFormat.py Path_To_Input.txt Path_to_output.txt
	Example: 
'''

import sys
import os

if __name__=="__main__":
	args = sys.argv
	if len(args) != 3:
		print("Syntax : python toEvaluateFormat.py Path_To_Input.txt Path_to_output.txt")
		sys.exit(1)

	input_filename = args[1]
	output_filename = args[2]

	with open(input_filename, "r") as input_file:
		output = ""
		lines = input_file.readlines()
		for line in lines:
			tokens = line.split(" ")
			for word in tokens:
				if word == "\n":
					continue
				if word.split("/")[1] == "O": #cas du tag /O : on enleve le tag
					output += word.replace("/O","")
				else:   #cas des autres étiquettes : on remplace le / par un _
					output += word.replace("/", "_")
				output += " "
			output += "\n"

	with open(output_filename, "w") as output_file:
			output_file.write(output)