# -*- encoding: utf8 -*-
import codecs
from monakeb.utils import DB_PATH

current = set()
khalil = set()

def load_roots():
  with codecs.open(DB_PATH + 'roots.txt', 'r', 'utf8') as current_file:
    for current_line in current_file:
      if not current_line.isspace():
        current.add(current_line.strip())
  with codecs.open(DB_PATH + 'khalil_roots.txt', 'r', 'cp1256') as khalil_roots:
    for khalil_line in khalil_roots:
      root, index = khalil_line.split()
      khalil.add(root)
  return current, khalil

extras = []
current, khalil = load_roots()
for root in khalil:
  if root not in current:
    extras.append(root)

print len(extras)
# with codecs.open(DB_PATH + 'new_roots.txt', 'w', 'utf8') as new:
#   for root in extras:
#     new.write(root + '\n')

with codecs.open(DB_PATH + 'roots.txt', 'a', 'utf8') as new_roots:
  for root in extras:
    new_roots.write(root + '\n')