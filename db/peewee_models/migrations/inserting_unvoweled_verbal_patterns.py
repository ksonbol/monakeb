from ..verbs import *
import xml.etree.ElementTree as ET
from peewee import *


for i in range(2, 10):
	path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db" \
	               "/verbs/patterns/Unvoweled/UnvoweledVerbalPatterns" + str(i) + ".xml"
	tree = ET.parse(path_to_file)
	root = tree.getroot()
	unvoweled_ver_patterns = []

	for child in root:
		attr = child.attrib
		unvoweled_ver_patterns.append(UnvoweledVerbalPattern(value = attr['value'],
									rules = attr['rules'], pat_num = i,
				 					ids = attr['ids']))

	print 'UnvoweledVerbalPatterns' + str(i) + ' created'

	for pattern in unvoweled_ver_patterns:
		pattern.save()

	print 'UnvoweledVerbalPatterns' + str(i) + ' saved'
	print

print "Success !"



