# -*- encoding: utf8 -*-

from utils import DB_PATH
import codecs, booby
from booby import Model, fields, serialize

CHARS = u'ءبتثجحخدذرزسشصضطظعغفقكلمنهوي'

def load(file_name):
    with codecs.open(DB_PATH + file_name + '.txt', 'r', 'utf8') as f:
        objects = serialize.deserialize(f)
    return objects

def load_patterns(file_name_prefix):
    patterns = {}
    for i in range(2, 10):
        file_name = DB_PATH + file_name_prefix + str(i) + ".txt"
        with codecs.open(file_name, 'r', 'utf8') as f:
            patterns[i] = serialize.deserialize(f)
    return patterns

def load_roots():
    roots = set()
    with codecs.open(DB_PATH + 'roots.txt', 'r', 'utf8') as f:
        for line in f:
            if not line.isspace():
                line = line.strip()
                roots.add(line)
    return roots

def load_nominal_roots():
  roots_path = DB_PATH + 'roots/nominal_roots/'
  nominal_roots = {}
  for char in CHARS:
    file_path = roots_path + char + '.txt'
    nominal_roots[char] = {}
    with codecs.open(file_path, 'r', 'utf8') as f:
      tmp_roots = serialize.deserialize(f)
    for root in tmp_roots:
      nominal_roots[char][root.value] = root
  return nominal_roots

def load_verbal_roots():
  roots_path = DB_PATH + 'roots/verbal_roots/'
  verbal_roots = {}
  for char in CHARS:
    file_path = roots_path + char + '.txt'
    verbal_roots[char] = {}
    with codecs.open(file_path, 'r', 'utf8') as f:
      tmp_roots = serialize.deserialize(f)
    for root in tmp_roots:
      verbal_roots[char][root.value] = root
  return verbal_roots