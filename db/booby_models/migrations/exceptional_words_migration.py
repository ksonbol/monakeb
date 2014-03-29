# -*- encoding:utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.special_words import ExceptionalWord
from ..booby_models import ExceptionalWordB

OUT_FILE = '/home/karim/monakeb/db/booby_models/exceptional_words.txt'

words = []
query = ExceptionalWord.select()
for word in query:
	new_word = ExceptionalWordB(unvoweled_form = word.unvoweled_form,
															voweled_form = word.voweled_form,
															prefix = word.prefix,
															stem = word.stem,
															word_type = word.word_type,
															suffix = word.suffix)
	words.append(new_word)

print len(words)
with codecs.open(OUT_FILE, 'w', 'utf8') as f:
	serialize.serialize(words, f)