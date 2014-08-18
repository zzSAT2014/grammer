#access to current and super-level modules
import sys
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))
from csv_reader import readcsv
from mysql import database


def option_convert(lis):
	''' lis <--- ['1', '2 ,3,4', '2', '2', '2']
		output---> a list of all indivudal atoms'''

	result = set([])
	for atom in lis:
		ele = atom.split(',')
		ele = set(map(eval,ele))
		
		result.update(ele)
	return list(result)


#print option_convert(['1', '2 ,3,4', '2', '2', '2'])

def process_input_data(lis):
	'''input: [a list of individual rows]
				e.g [['id ', 'A', 'B', 'C', 'D', 'E'], ['10001', '1', '2 ,3,4', '2', '2', '2'], ['10002', '1', '2', '3', '4', '5']]

		output: 
				result---> list of tuples for insertion 
							[(col_names, col_values).....]
			'''

	index_convertor = lambda a: (int(a[0:-2]), int(a[-2:]))
	type_convertor = lambda num: 'type%s'%(num)
	lis =lis[1:] #get rid of header
	result =[]
	for row in lis:
		id,val = row[0],row[1:]
		
		serial_no,question_no = index_convertor(id)
		types = option_convert(val)

		key = ['serial_no', 'question_no']
		key_type = map(type_convertor,types)
		key += key_type
		value = [serial_no,question_no] + [1,]*len(types)
		value = map(str,value)
		atom = (key,value)
		result.append(atom)
	return result







filename ='/Users/Zhe/Desktop/grammer/bank_trial.csv'

input_data = readcsv(filename)
data = process_input_data(input_data)
mydb = database('test')
mydb.simple_insert('grammer_bank',data)

