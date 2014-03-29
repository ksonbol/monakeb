# -*- coding: utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.nouns import UnvoweledNominalPattern
from ..booby_models import *

words = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
query = UnvoweledNominalPattern.select()
for word in query:
	pat_num = word.pat_num
	new_word = UnvoweledNominalPatternB(value = word.value,
																			rules = word.rules,
																			ids = word.ids,
																			pat_num = word.pat_num)
	words[pat_num].append(new_word)

for i in range(2, 10):
	OUT_FILE = "/home/karim/monakeb/db/booby_models/nouns/unvoweled_nominal_patterns%s.txt" %i
	print i, len(words[i])
	with codecs.open(OUT_FILE , 'w', 'utf8') as f:
		serialize.serialize(words[i], f)