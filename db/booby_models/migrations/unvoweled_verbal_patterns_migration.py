# -*- coding: utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.verbs import UnvoweledVerbalPattern
from ..booby_models import *
from monakeb.utils import DB_PATH

words = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
query = UnvoweledVerbalPattern.select()
for word in query:
	pat_num = word.pat_num
	new_word = UnvoweledVerbalPatternB(value = word.value,
																		rules = word.rules,
																		ids = word.ids,
																		pat_num = word.pat_num)
	words[pat_num].append(new_word)


for i in range(2, 10):
	OUT_FILE = DB_PATH + "verbs/unvoweled/unvoweled_verbal_patterns%s.txt" %i
	print i, len(words[i])
	with codecs.open(OUT_FILE , 'w', 'utf8') as f:
		serialize.serialize(words[i], f)