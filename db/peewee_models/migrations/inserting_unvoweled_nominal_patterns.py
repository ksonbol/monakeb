from ..nouns import *
import xml.etree.ElementTree as ET
from peewee import *


for i in range(2, 10):
	path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/nouns/patterns" \
                   "/Unvoweled/UnvoweledNominalPatterns" + str(i) + ".xml"
	tree = ET.parse(path_to_file)
	root = tree.getroot()
	unvoweled_nom_patterns = []

	for child in root:
		attr = child.attrib
		unvoweled_nom_patterns.append(UnvoweledNominalPattern(value = attr['value'],
									rules = attr['rules'], pat_num = i,
				 					ids = attr['ids']))

	print 'UnvoweledNominalPatterns' + str(i) + ' created'

	for pattern in unvoweled_nom_patterns:
		pattern.save()

	print 'UnvoweledNominalPatterns' + str(i) + ' saved'
	print


