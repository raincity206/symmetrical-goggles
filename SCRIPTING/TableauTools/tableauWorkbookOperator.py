from tableaudocumentapi import Workbook
from tableaudocumentapi import Datasource
from tableaudocumentapi import Field
from tableaudocumentapi import Connection

import pprint as pp


sourceWB = Workbook('ZenoWorkbook.twb')
sourceDB = Datasource.from_file('Beatlog (BeatlogV1).tdsx')

print("Filename: " +sourceWB.filename)
print(sourceWB.worksheets)
pp.pprint(sourceWB.datasources)

def listTDS(sourceTDS):
	print('----------------------------------------------------------')
	print('-- Info for our .tds:')
	print('--   name:\t{0}'.format(sourceTDS.name))
	print('--   version:\t{0}'.format(sourceTDS.version))
	print('----------------------------------------------------------')
	return



pp.pprint(sourceDB.connections)

pp.pprint(sourceDB.fields)

def showFields(sourceTDS):
	print('----------------------------------------------------------')
	print('--- {} total fields in this datasource'.format(len(sourceTDS.fields)))
	print('----------------------------------------------------------')
	for count, field in enumerate(sourceTDS.fields.values()):
	    print('{:>4}: {} is a {}'.format(count+1, field.name, field.datatype))
	    blank_line = False
	    if field.calculation:
	        print('      the formula is {}'.format(field.calculation))
	        blank_line = True
	    if field.default_aggregation:
	        print('      the default aggregation is {}'.format(field.default_aggregation))
	        blank_line = True
	    if field.description:
	        print('      the description is {}'.format(field.description))

	    if blank_line:
	        print('')
	print('----------------------------------------------------------')
	return


showFields(sourceDB)
listTDS(sourceDB)
"""
db = ""
sourceDB = ""
count = 1

#Importing Datasource object from the workbook
for j in sourceWB.datasources:
	print("Datasource " + str(count))
	for x in j.connections:
		db = x.dbclass
	sourceDB = Datasource.from_connections (db, j.connections)

	#Printing information about the datasource
	print("Connection information :")
	print(sourceDB.connections)
	print("Datasource caption :")
	print(sourceDB.caption)
	print""
	print("Tableau version :")
	print(sourceDB.version)
	print(sourceDB.caption)
	
	#Printing information about the field
	print("Information about fields in this order (name, id, caption, alias, datatype, role, calculation, is quantitative?, is ordinal?, is nominal?, worksheets used in, default aggregation :")
	for x in sourceDB.fields.values():

	print ""
	print ""
	count = count+1

"""
