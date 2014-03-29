# import codecs
# file_path = "/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/prefixes.xml"
# prefixes_xml = codecs.open(file_path, "r", "cp1256")


from special_words import ToolWord
import xml.etree.ElementTree as ET
from peewee import *

# ToolWord.create_table()
# Migrations 
tree = ET.parse("/home/karim/Python Projects/Pykhalil-lib/AlKhalil1.1/db/specialwords/toolwords.xml")
root = tree.getroot()
tool_words = []
for child in root[3:7]:
	attr = child.attrib
	tool_words.append(ToolWord(unvoweled_form = attr['unvoweledform'], voweled_form = attr['voweledform'], 
						word_type = attr['type'], prefix_class = attr['prefixeclass'],
			 			suffix_class = attr['suffixeclass'], priority = attr['priority']))
	for word in tool_words:
		word.save()