
import re
import time
import pandas as pd
import dateutil



def open_file(filename):
		x = open(filename,'r')
		y = x.read()
		content = y.splitlines()
		return content
		
		
def ismessage(str):
		patterns = {

		"hor1":r'w{3}s{1}[0-9]{1,2},s{1}d{4},s{1}d{2}:d{2}', 
		"hor2":r'w{3}s{1}[0-9]{1,2},s{1}d{2}:d{2}', 
		"imp2":r'd{1,2}sw{3}sd{2}:d{2}', 
		"imp1":r'd{1,2}sw{3}sd{4}sd{2}:d{2}'

		}
		for key in patterns:
			result = re.search(patterns[key], str)
			if result and str.count(':') >=2:
				name_start = str.find("-")+2
				first_colon = str.find(":")
				name_end = str.find(":", first_colon+1)
				name=str[name_start:name_end]
				message=str[name_end+1:]
				return [name, message, result.group()]
		return ["","",str]
		
		

def process(self,content):
		j = 1
		df = pd.DataFrame(index = range(1, len(content)+1), columns=[ 'Name', 'Message', 'date_string'])
		for i in content:
			results = self.ismessage(i)
			if results[0] != "":
				df.ix[j]=results
			else:
				df.ix[j]['Name']=df.ix[j-1]['Name']
				df.ix[j]['date_string']=df.ix[j-1]['date_string']
				df.ix[j]['Message']=results[2]
			j = j+1
		df['Time'] = df['date_string'].map(lambda x: dateutil.parser.parse(x))
		df['Day'] = df['date_string'].map(lambda x: dateutil.parser.parse(x).strftime("%a"))
		df['Date'] = df['date_string'].map(lambda x:dateutil.parser.parse(x).strftime("%x"))
		df['Hour'] = df['date_string'].map(lambda x:dateutil.parser.parse(x).strftime("%H"))
		
		



lines = open_file('data.txt')
print ismessage(lines[0])
