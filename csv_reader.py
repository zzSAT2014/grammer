import csv

#access to current and super-level modules
import sys
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

def readcsv(filename):
	'''input: 
		filename <--- complete path of a csv file


		output: 
			result---> [a list of individual rows], perservation of individual box if len(box)>0
			e.g [['id ', 'A', 'B', 'C', 'D', 'E'], ['10001', '1', '2 ,3,4', '2', '2', '2'], ['10002', '1', '2', '3', '4', '5']]'''

	file =  open(filename)
	empty_string = lambda atom: False if len(atom) == 0 else True
	iterable = csv.reader(file)
	result = []
	for line in iterable:
		line = filter(empty_string,line)
		#print line
		if len(line)>0:
			result.append(line)
	return result

#print readcsv('/Users/Zhe/Desktop/grammer/csvtrial.csv')