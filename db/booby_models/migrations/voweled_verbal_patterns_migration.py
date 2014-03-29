# -*- coding: utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.verbs import VoweledVerbalPattern
from ..booby_models import *

words = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
query = VoweledVerbalPattern.select()
for word in query:
	pat_num = word.pat_num
	new_word = VoweledVerbalPatternB(	pat_id = word.pat_id,
																		diac = word.diac,
																		canonic = word.canonic,
																		pat_type = word.pat_type,
																		pat_num = word.pat_num,
																		aug = word.aug,
																		cas = word.cas,
																		ncg = word.ncg,
																		trans = word.trans)
	words[pat_num].append(new_word)


for i in range(2, 10):
	OUT_FILE = "/home/karim/monakeb/db/booby_models/verbs/voweled/voweled_verbal_patterns%s.txt" %i
	print i, len(words[i])
	with codecs.open(OUT_FILE , 'w', 'utf8') as f:
		serialize.serialize(words[i], f)