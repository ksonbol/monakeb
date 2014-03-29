from ..prefixes import *
from ..suffixes import *
from peewee import *
import xml.etree.ElementTree as ET


# Inserting prefixes

path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/prefixes.xml"
tree = ET.parse(path_to_file)
root = tree.getroot()
prefixes = []

for child in root:
	attr = child.attrib
	prefixes.append(Prefix(unvoweled_form = attr['unvoweledform'],
							voweled_form = attr['voweledform'], description = attr['desc'],
							p_class = attr['classe']))

print "Prefixes created !"

for prefix in prefixes:
	prefix.save()

print "Prefixes saved !"

# insering suffixes

path_to_file = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/suffixes.xml"
tree = ET.parse(path_to_file)
root = tree.getroot()
suffixes = []

for child in root:
	attr = child.attrib
	suffixes.append(Suffix(unvoweled_form = attr['unvoweledform'],
							voweled_form = attr['voweledform'], description = attr['desc'],
							s_class = attr['classe']))

print "Suffixes created !"

for suffix in suffixes:
	suffix.save()

print "Suffixes saved !"