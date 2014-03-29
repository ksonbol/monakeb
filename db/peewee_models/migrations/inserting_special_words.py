from ..special_words import *
import xml.etree.ElementTree as ET
from peewee import *

# inserting tool words
tree = ET.parse("/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/specialwords/toolwords.xml")
root = tree.getroot()
tool_words = []

for child in root:
	attr = child.attrib
	tool_words.append(ToolWord(unvoweled_form = attr['unvoweledform'], voweled_form = attr['voweledform'], 
						word_type = attr['type'], prefix_class = attr['prefixeclass'],
			 			suffix_class = attr['suffixeclass'], priority = attr['priority']))


for word in tool_words:
	word.save()

# inserting exceptional words
tree = ET.parse("/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/specialwords/exceptionalwords.xml")
root = tree.getroot()
exceptional_words = []

for child in root:
	attr = child.attrib
	exceptional_words.append(ExceptionalWord(unvoweled_form = attr['unvoweledform'],
											voweled_form = attr['voweledform'], 
											prefix = attr['prefix'], stem = attr['stem'], 
											word_type = attr['type'], suffix = attr['suffix']))

for word in exceptional_words:
	word.save()

# inserting proper nouns
tree = ET.parse("/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/specialwords/propernouns.xml")
root = tree.getroot()
proper_nouns = []

for child in root:
	attr = child.attrib
	proper_nouns.append(ProperNoun(unvoweled_form = attr['unvoweledform'],
									voweled_form = attr['voweledform'], 
									noun_type = attr['type']))

for word in proper_nouns:
	word.save()

print 'Success!'