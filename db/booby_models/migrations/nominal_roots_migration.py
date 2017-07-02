# -*- encoding: utf8 -*-

import booby, codecs, os
from booby import Model, fields, serialize
from monakeb.db.peewee_models.nouns import NominalRoot
from monakeb.utils import DB_PATH
from ..booby_models import NominalRootB

CHARS = u'ءبتثجحخدذرزسشصضطظعغفقكلمنهوي'
DIRECTOTY = DB_PATH + 'roots/nominal_roots/'

for char in CHARS:
  query = NominalRoot.select().where(NominalRoot.char == char)
  out_file = DIRECTOTY + char + ".txt"
  roots = []
  for root in query:
    new_root = NominalRootB(value = root.value, vect = root.vect, 
                            root_type = root.root_type, char = root.char)
    roots.append(new_root)
  with codecs.open(out_file, 'w', 'utf8') as f:
    serialize.serialize(roots, f)