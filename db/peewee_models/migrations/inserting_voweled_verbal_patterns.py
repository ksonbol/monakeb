from ..verbs import *
import xml.etree.ElementTree as ET
from peewee import *


for i in range(2, 10):
	path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1" \
	               "/db/verbs/patterns/Voweled/VoweledVerbalPatterns" + str(i) + ".xml"
	tree = ET.parse(path_to_file)
	root = tree.getroot()
	voweled_ver_patterns = []

	for child in root:
		attr = child.attrib
		voweled_ver_patterns.append(VoweledVerbalPattern(pat_id = attr['id'],
									diac = attr['diac'], canonic = attr['canonic'],
									pat_type = attr['type'], pat_num = i,
									aug = attr['aug'], cas = attr['cas'], 
									ncg = attr['ncg'], trans = attr['trans']
									))

	print 'VoweledVerbalPatterns' + str(i) + ' created'

	for pattern in voweled_ver_patterns:
		pattern.save()

	print 'VoweledVerbalPatterns' + str(i) + ' saved'
	print

print "Success!"


