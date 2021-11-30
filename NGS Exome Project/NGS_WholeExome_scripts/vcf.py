#!/usr/bin/env python3

import time
import sys 
import os
import re 

# If the user forgets to put the path to the directory, an error message is printed and the code is terminated 
if len(sys.argv) < 2:
	sg.popup('Please provide the path to the directory containing the vcf files as a command line argument !',
				title = 'ERROR', background_color = 'black', text_color = 'red', font = 50)  
	exit()
# If the user enters more than on argument after the script file name and the path to the directory, an error message is printed and the code is terminated 
elif len(sys.argv) > 2:
	sg.popup('Wrong number of arguments. Make sure to ONLY provide the path to the directory containing containing the vcf files',
				title = 'ERROR', background_color = 'red', text_color = 'black', font = 50)
	exit()
# If the user correctly provides the path to the directory, it is saved in the variable directory_path
else:
	directory_path = sys.argv[1]

# Loops into each of the directory's content 
for file in os.listdir(directory_path):
	# Disregard any item that is not a file 
	if os.path.isfile(os.path.join(directory_path, file)):

		# Diregard any file that is not a vcf file or zipped file
		if file.lower().endswith(".vcf") or file.lower().endswith(".vcf.gz"):
			# Open file in read mode 
			current_file = open(directory_path + file, "r")
			# Stores the lines of the file in a list, diregarding \n lines 
			file_lines = [line.rstrip('\n') for line in current_file]
			header = []
			info_meta_info = []
			filter_meta_info = [] 
			format_meta_info = []
			body = []

			for line in range(len(file_lines)):
				if(re.match('^\#\#', file_lines[line], re.MULTILINE)):
					header.append(line)

					if(re.match('^\#\#INFO', file_lines[line], re.MULTILINE)):
						info_meta_info.append(file_lines[line])

					elif (re.match('^\#\#FILTER', file_lines[line], re.MULTILINE)):
						filter_meta_info.append(file_lines[line])

					elif (re.match('^\#\#FORMAT', file_lines[line], re.MULTILINE)):
						format_meta_info.append(file_lines[line])

				elif (re.match('^\#CHROM', file_lines[line], re.MULTILINE)):
					fixed_fields = (file_lines[line]).split("\t")
				else:
					body.append(file_lines[line])

			CHROM = []
			POS = [] 
			ID = [] 
			REF = [] 
			ALT = [] 
			QUAL = [] 
			FILTER = [] 
			INFO = []

			body_info = [] 
			for i in body:
				body_info = i.split("\t")
				CHROM.append(body_info[0])
				POS.append(body_info[1])
				ID.append(body_info[2])
				REF.append(body_info[3])
				ALT.append(body_info[4])
				QUAL.append(body_info[5])
				FILTER.append(body_info[6])
				INFO.append(body_info[7])



			





								