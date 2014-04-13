# -*- encoding:utf8 -*-

import booby, codecs
from booby import Model, fields, serialize
from monakeb.db.peewee_models.prefixes import *
from ..booby_models import PrefixB
from monakeb.utils import DB_PATH

OUT_FILE = DB_PATH + 'prefixes.txt'

prefixes = []
query = Prefix.select()
for prefix in query:
	new_pref = PrefixB(unvoweled_form = prefix.unvoweled_form,
											voweled_form = prefix.voweled_form,
											description = prefix.description,
											p_class = prefix.p_class)
	prefixes.append(new_pref)

print len(prefixes)
with codecs.open(OUT_FILE, 'w', 'utf8') as f:
	serialize.serialize(prefixes, f)