# -*- encoding:utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.suffixes import *
from ..booby_models import SuffixB
from monakeb.utils import DB_PATH

OUT_FILE = DB_PATH + 'suffixes.txt'

suffixes = []
query = Suffix.select()
for suffix in query:
	new_suff = SuffixB(unvoweled_form = suffix.unvoweled_form,
											voweled_form = suffix.voweled_form,
											description = suffix.description,
											s_class = suffix.s_class)
	suffixes.append(new_suff)

print len(suffixes)
with codecs.open(OUT_FILE, 'w', 'utf8') as f:
	serialize.serialize(suffixes, f)