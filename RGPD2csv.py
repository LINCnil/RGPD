from __future__ import unicode_literals
import codecs
from ruffus import *
import csv
import re
import string

@files('RGPD_art.txt', 'RGPD_artutf8.txt')
def sample(infile, outfile):
	with open(infile, 'r') as f:
#		lines = [line for i,line in enumerate(f.readlines()) if i<50]
		lines = f.readlines()
	with codecs.open(outfile, 'w', encoding='utf-8') as f:
		for line in lines:	
			f.write(line.decode("latin1"))

@follows(sample)
@files('RGPD_artutf8.txt', 'RGPD_art.tsv')
def extract(infile, outfile):
	g = codecs.open(outfile, 'w', encoding='utf-8')
	with codecs.open(infile, 'r', encoding='utf-8') as f:
		lines = f.readlines()
		str=""
		newline = False
		foundArticle = False
		for line in lines:
			if line.find('Article') != -1:
				if newline == True:
					g.write("\"" + str + "\"\n")
				newline = False
				foundArticle = True
				str=""
				Art = line.strip()
				g.write("\"" + Art + "\"\t")
			else:
				if foundArticle == True:
					Obj = line.strip()
					g.write("\"" + Obj + "\"\t")
					foundArticle = False
					newline = True
				else:
					if len(line) != 2:
						str+=line
						newline = True
					#print str


def __main__():
	pipeline_run([extract])

if __name__ == '__main__':
	__main__()  
