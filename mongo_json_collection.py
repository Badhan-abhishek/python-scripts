import os
import sys

# To be tested with CSV data 
# file_type = int(input('''
# 	Please choose file type
# 	1) JSON
# 	2) CSV
# 	Type down number as option:
# 	'''))
# if file_type != 1 and file_type != 2:
# 	sys.exit('Wrong selection')
	
# Get directory path
directory = input("Please enter valid directory where json files exists: ")

# Get DB name from user
db = input("Enter your db name: ")

# Get files from current folder system
file_name = [f for f in os.listdir(directory) if f.endswith('.json')]

print(file_name)

# Empty array to fill names without any extension
only_name = []

for i in file_name:
	txt = i.split('.')
	command = 'cd {directory} && mongoimport --db trackyou --collection {collection_name} --file {json_name}'.format(collection_name=txt[0], json_name=i, directory=directory)
	print(command)
	os.system(command)
