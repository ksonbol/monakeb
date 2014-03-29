from ..nouns import *
import xml.etree.ElementTree as ET
from peewee import *
import os

# inserting roots
for i in range(1, 3):
	print "Inserting nominal roots " + str(i) + ".."
	print "--------------------------------"
	print 
	path = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/nouns/roots" + str(i) + "/"
	l = os.listdir(path)
	for file_name in l:
		char = file_name.rstrip(".xml")
		path_to_file = path + file_name
		tree = ET.parse(path_to_file)
		root = tree.getroot()
		roots = []
		print "Creating roots.."
		print char
		for child in root:
			attr = child.attrib
			roots.append(NominalRoot(value = attr['val'] , vect = attr['vect'],
									root_type = i, char = char))
		print "Roots created"
		print
		print "Saving roots.."

		for root in roots:
			root.save()

		print "Roots saved"
		print

print "Success !"