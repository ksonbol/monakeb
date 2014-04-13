# -*- coding: utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.nouns import VoweledNominalPattern
from ..booby_models import *
from monakeb.utils import DB_PATH

words = {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
query = VoweledNominalPattern.select()
for word in query:
	pat_num = word.pat_num
	new_word = VoweledNominalPatternB(pat_id = word.pat_id,
																		diac = word.diac,
																		canonic = word.canonic,
																		pat_type = word.pat_type,
																		cas = word.cas,
																		ncg = word.ncg,
																		pat_num = word.pat_num)
	words[pat_num].append(new_word)


for i in range(2, 10):
	OUT_FILE = DB_PATH + "nouns/voweled_nominal_patterns%s.txt" %i
	print i, len(words[i])
	with codecs.open(OUT_FILE , 'w', 'utf8') as f:
		serialize.serialize(words[i], f)