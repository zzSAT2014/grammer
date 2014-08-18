#access to current and super-level modules
import sys
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))
from csv_reader import readcsv
from mysql import database



def process_input_data(lis):
	'''input: 
		lis <-- lis of records
				e.g :[['Name', 'Date', 'Serial No.', 'Question No.'],['Zhixiang Du', '2014-8-15', '407', '1,2,3,4'], ['Zhixiang Du', '2014-8-16', '506', '5,6,7,8']

		output:
			result --> list of individual records [['Zhixiang Du', '2014-8-15', '407', '1']...]'''
	result = []
	lis = lis[1:] #get rid of header
	for record in lis:
		name,date,serial_no,questions = record
		questions = questions.split(',') 
		name = '\"%s\"'%name
		date = '\"%s\"'%date
		quesitons = map(str,map(int,questions)) #reduce to most simple int format
		for question in questions:
			result.append([name,date,serial_no,question])
	return result












filename = '/Users/Zhe/Desktop/grammer/record_trial.csv'
input_data = readcsv(filename)
#print input_data
data = process_input_data(input_data)
print data
mydb = database('test')
cols = ['student_name','record_date', 'serial_no', 'question_no']

mydb.simple_insert('grammer_record',cols, data )


