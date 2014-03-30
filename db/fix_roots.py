# -*- encoding:utf8 -*-
import codecs

def show_repeated():
  roots = set()
  repeated = set()
  with codecs.open('/home/karim/monakeb/db/booby_models/roots.txt', 'r+w', 'utf8') as f:
    for line in f:
      if not line.isspace():
        line = line.strip()
        if line in roots:
          repeated.add(line)
        else:
          roots.add(line)

  print "Repeated roots:"
  for root in repeated:
    print root

def show_extras():
  current_letter = u'أ'
  count = 0
  with codecs.open('/home/karim/monakeb/db/booby_models/roots.txt', 'r+w', 'utf8') as f:
    for line in f:
      if not line.isspace():
        line = line.strip()
        count += 1
        if line[0] != current_letter:
          print "finished: ", current_letter
          print "starting:", line[0], "after:", count
          count = 0
          current_letter = line[0]

if __name__ == '__main__':
  show_extras()