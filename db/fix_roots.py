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

  print len(repeated), "Repeated roots:"
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

def normailize_hamza():
  with codecs.open('/home/karim/monakeb/db/booby_models/roots.txt', 'r+w', 'utf8') as f:
    with codecs.open('/home/karim/monakeb/db/booby_models/roots2.txt', 'a', 'utf8') as w:
      for line in f:
        new_line = line.replace(u'أ', u'ء')
        w.write(new_line)

if __name__ == '__main__':
  show_repeated()