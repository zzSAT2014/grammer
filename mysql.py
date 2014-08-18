#access to current and super-level modules
import sys
import os
subdir = os.path.dirname(__file__)
sys.path.append(subdir)
sys.path.append(os.path.abspath(os.path.join(subdir, os.pardir)))

import MySQLdb as mysqldb

class database(object):
	def __init__(self,database,passwd ='',host = 'localhost', user = 'root'):
		'''connect to database'''

		self.db = mysqldb.connect(host = host,
                      				user = user,
                      				passwd = passwd,
                      				db = database
									)
		self.cur = self.db.cursor()

	def simple_insert(self,table, col, value ):
		'''input:
			table <--- table name, str
			cols <--- fixed columns to be inserted, lis
			values <--- value to be inserted in each row, lis [[1],[2]...]

			output:
				Nil'''

		result = []
		for row in value:
			result.append((col,row))
		self.insert(table,result)


	def insert(self,table, lis):
		'''input:
			table <--- table name, str
			lis  <--- [(col_names. col_values).....]

			insert value into table

			output:
			Nil'''

		for row in lis:
			col , val = row 

			#terminate
			if not len(col)== len(val): 
				print 'invalid input, terminate process'
				return None 

			format = lambda lis: "(%s)"%','.join(lis)

			col,val = format(col),format(val)
			key = table + col
			value = 'values' + val
			statement = '''insert into %s %s'''%(key,value)
			try: self.cur.execute(statement)
			except: 
				print 'duplicate input %s' %(statement)
				
		self.cur.close()

		self.db.commit()






def test_db():
	a = database('test')
	table = 'grammer_bank'
	value =	[(['question_id'],['1'])]
	a.simple_insert(table,['question_id'],[['1'],['2'],['3']])


#test_db()









