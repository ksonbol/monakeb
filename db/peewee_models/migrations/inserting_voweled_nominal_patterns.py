from ..nouns import *
import xml.etree.ElementTree as ET
from peewee import *


for i in range(2, 10):
	path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/nouns/patterns" \
                   "/Voweled/VoweledNominalPatterns" + str(i) + ".xml"
	tree = ET.parse(path_to_file)
	root = tree.getroot()
	voweled_nom_patterns = []

	for child in root:
		attr = child.attrib
		voweled_nom_patterns.append(VoweledNominalPattern(pat_id = attr['id'],
									diac = attr['diac'], canonic = attr['canonic'],
									pat_type = attr['type'], pat_num = i,
									cas = attr['cas'], ncg = attr['ncg']
									))

	print 'VoweledNominalPatterns' + str(i) + ' created'

	for pattern in voweled_nom_patterns:
		pattern.save()

	print 'VoweledNominalPatterns' + str(i) + ' saved'
	print


