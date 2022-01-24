
if __name__ == '__main__':
	import pandas as pd
	import scipy as sp
	import numpy as np
	import matplotlib as plt
	import pyDOE2 as doe
	import re


class ExperimentalPlan():
    pass


class ShimdazuParser():
    """A Toolkit for extraction of data from the exported ASCII-files."""
    def __init__(self,file="ASCIIExport.txt"):
        self.file = str("file")
    
    def extractRetentionViaMaxima():
        '''Method Development'''
        pass
    
    def extractBlanks():
        '''Quality Control'''
        pass
    
    def extractControls():
        pass
    
    def extractConcentrations():
        '''Searches for Strings which indicate an measured analyte in the ASCII-File. Then tries to extract 
        the concentration evaluated by the Shimdazu LabSolution-Software and brings the extracted data in a 
        table with a column for sample-Names and a new column for every analyte.'''
        
		global tempF
		i = int(0)
		n = int(0)
		ctr1 = bool("false")
		results = {}
		namelines = []
		samplelines = []
		regex1 = str('Name\t')
		regex2 = str('Data Filename')
		regex3 = str('\d\t')
		regex4 = str('.lcd\t')

		with open('ascii.txt','r+') as exfile:
			for line in exfile:
				line = str(line)
				i = int(i+1)
				print(">>> Line "+str(i)+"...")
				if regex1 in line:
					if regex2 not in line:
						n = int(n+1)
						analyte = line[5:]
						analyte = analyte[:-1]
						namelines.append(analyte)
						print("1: Substance-Pattern for >> "+analyte+" << found in line "+str(i)+".")
					elif regex2 in line:
						header =  line.split("\t")
				if ctr1 == bool("true"):
					if regex4 in line:
						print("2: Sample-Value found in line "+str(i)+".")
						line = line.split("\t")
						samplelines.append(line)
					else: 
						ctr1 = bool("false")
						if (n<2):				
							#Write Sample-Name-Column to the DataFrame
							pass
						else:
							#Write a Column with the Analyte-Name to the DataFrame
							#Write specific Conc.-Values to the new column.
							tempF = pd.DataFrame(samplelines)
							tempF.columns = header
							return tempF
				return 
		

class ControlChart(self,typ):
    pass		

class ChromPlots():
    pass


def extractValues():
    global tempF
	i = int(0)
	n = int(0)
	ctr1 = bool("false")
	results = {}

	with open('ascii.txt','r+') as exfile:
		for line in exfile:
			line = str(line)
			i = int(i+1)
			print(">>> Line "+str(i)+"...")
			if regex1 in line:
				if regex2 not in line:
					n = int(n+1)
					analyte = line[5:]
					analyte = analyte[:-1]
					namelines.append(analyte)
					print("1: Substance-Pattern for >> "+analyte+" << found in line "+str(i)+".")
				elif regex2 in line:
					header =  line.split("\t")
			if ctr1 == bool("true"):
				if regex4 in line:
					print("2: Sample-Value found in line "+str(i)+".")
					line = line.split("\t")
					samplelines.append(line)
				else: 
					ctr1 = bool("false")
					if (n<2):				
						#Write Sample-Name-Column to the DataFrame
						pass
					else:
						#Write a Column with the Analyte-Name to the DataFrame
						#Write specific Conc.-Values to the new column.
						tempF = pd.DataFrame(samplelines)
						tempF.columns = header
						return tempF
			return 

extractValues()
print("")					
print("")
print("")					
print("")
print("")					
print("")
print("Temporary DataFrame for single substance:")					
print(tempF)

print(namelines)
print("")
print(samplelines)

exit()

'''
df1.append(df2)
'''
