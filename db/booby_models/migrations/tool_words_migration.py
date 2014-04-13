# -*- encoding:utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.special_words import ToolWord
from ..booby_models import ToolWordB
from monakeb.utils import DB_PATH

OUT_FILE = DB_PATH + 'tool_words.txt'

words = []
query = ToolWord.select()
for word in query:
	new_word = ToolWordB(	unvoweled_form = word.unvoweled_form,
												voweled_form = word.voweled_form,
												word_type = word.word_type,
												prefix_class = word.prefix_class,
												suffix_class = word.suffix_class,
												priority = word.priority)
	words.append(new_word)

print len(words)
with codecs.open(OUT_FILE, 'w', 'utf8') as f:
	serialize.serialize(words, f)