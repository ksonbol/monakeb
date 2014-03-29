# -*- encoding:utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.special_words import ProperNoun
from ..booby_models import ProperNounB

OUT_FILE = '/home/karim/monakeb/db/booby_models/proper_nouns.txt'

words = []
query = ProperNoun.select()
for word in query:
	new_word = ProperNounB(	unvoweled_form = word.unvoweled_form,
												voweled_form = word.voweled_form,
												noun_type = word.noun_type)

	words.append(new_word)

print len(words)
with codecs.open(OUT_FILE, 'w', 'utf8') as f:
	serialize.serialize(words, f)