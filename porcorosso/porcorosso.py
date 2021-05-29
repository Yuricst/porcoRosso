#!/usr/bin/env python3
"""
Porco Rosso themed functions
@Yuricst
"""

import time


def split_list(full_list, list_length):
	"""Split single list to multiple lists with certain length"""
	n_char = len(full_list)
	n_list = n_char // list_length + 1
	split_list = []
	for idx in range(n_list):
		if idx != n_list-1:
			split_list.append(full_list[idx*list_length:(idx+1)*list_length])
		else:
			split_list.append(full_list[idx*list_length:])
	return split_list


def merge_string(char_list):
	"""Merge characters in a list to single string"""
	for idx in range(len(char_list)):
		if idx==0:
			print_str = char_list[idx]
		else:
			print_str += char_list[idx]
	return print_str


def introduction(language="JPN"):
	"""Return introduction string in specified language"""
	intro_dict = {
		"JPN": "この映画は、飛行艇時代の地中海を舞台に、誇りと女と金をかけて空中海賊と戦い、紅の豚とよばれた一匹の豚の物語である。",
		"ENG": "This motion picture is set over the Mediterranean Sea in an age when seaplanes ruled the waves. It tells the story of a valiant pig, who fought against flying pirates, for his pride, for his lover, and for his fortune. The name of the hero of our story is Crimson Pig."
		}
	return intro_dict[language]


def printrosso(string, rowlength=16, keep=5, sleep=0.12, remove_sleep=0.08, newline_sleep=0.1, newline_end=True):
	"""Display string in Porco Rosso opening scene style

	Args:
		string (str): string to be printed
		rowlength (int): number of characters to fit in a single row
		keep (int): number of characters to keep at each new line
		sleep (float): time between each character
		remove_sleep (float): time between each character when removing line
		newline_sleep (float): sleep between lines
	"""
	# convert string to list of characters
	char_list = [char for char in string]

	# initialize while loop
	stop = False
	idx_row = 0
	while stop==False:
		# check if character is done or not
		if idx_row == 0: 
			if (idx_row+1)*rowlength < len(char_list):
				row_end_idx = (idx_row+1)*rowlength
			else:
				row_end_idx = len(char_list)
				stop = True
		else:
			if (idx_row+1)*rowlength < len(char_list):
				row_end_idx = (idx_row+1)*rowlength
			else:
				row_end_idx = len(char_list)
				stop = True

		# prepare row
		if idx_row == 0:   # first row
			row = char_list[idx_row*rowlength:row_end_idx]
		else:
			row = char_list[idx_row*rowlength-keep:row_end_idx]

		# display row
		for i in range(len(row)):
			#print_str = merge_string(row[0:i+1])
			print(merge_string(row[0:i+1]), end="\r")
			if idx_row == 0 or i > keep:
				time.sleep(sleep)

		# delete current line if not the final line
		if stop!=True:
			for j in range(len(row)-keep+1):
				#remove_tr = merge_string(row[j:])
				print(merge_string(row[j:]) + "  ", end="\r")
				time.sleep(remove_sleep)
		time.sleep(newline_sleep)

		# update index of rows printed
		idx_row += 1
	# go to new line
	if newline_end==True:
		print("\n")


# run function
if __name__=="__main__":
	string = introduction("JPN")
	printrosso(string)#, rowlength=16, keep=5, sleep=0.12, remove_sleep=0.08,

	#string = introduction("ENG")
	#printrosso(string, rowlength=46, keep=10, sleep=0.03, remove_sleep=0.03)
