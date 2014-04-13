# -*- encoding: utf8 -*-

from ..analyzer import *
import unittest

class TestExceptional(unittest.TestCase):
  def setUp(self):
    self.exceptional_words = load('exceptional_words')

  def test_match(self):
    word = u'بالله'
    self.assertEqual(u'الله', check_exceptional(word, self.exceptional_words))

  def test_mismatch(self):
    word = u'باله'
    self.assertIsNone(check_exceptional(word, self.exceptional_words))

class TestLoadPatterns(unittest.TestCase):
  def setUp(self):
    self.unvoweled_nouns = load_patterns('nouns/unvoweled/unvoweled_nominal_patterns')
    self.unvoweled_verbs = load_patterns('verbs/unvoweled/unvoweled_verbal_patterns')

  def test_count(self):
    self.assertEqual(len(self.unvoweled_nouns[2]), 3)
    self.assertEqual(len(self.unvoweled_nouns[5]), 237)
    self.assertEqual(len(self.unvoweled_verbs[4]), 120)
    self.assertEqual(len(self.unvoweled_verbs[9]), 26)

class TestLoadRoots(unittest.TestCase):
  def setUp(self):
    self.roots = load_roots()

  def test_length(self):
    roots_length = 9245
    self.assertEqual(len(self.roots), roots_length)

class TestBaseClass(unittest.TestCase):
  def setUp(self):
    self.prefixes = load('prefixes')
    self.suffixes = load('suffixes')

# SEGMEMTOR CLASS

class TestSegmentor(TestBaseClass):
  pass

# ANALYZER CLASS

class TestAnalyzer(TestBaseClass):
  def setUp(self):
    self.prefixes = load('prefixes')
    self.suffixes = load('suffixes_reversed')
    self.unvoweled_nouns = load_patterns('nouns/unvoweled/unvoweled_nominal_patterns')
    self.unvoweled_verbs = load_patterns('verbs/unvoweled/unvoweled_verbal_patterns')
    self.tool_words = load('tool_words')
    self.proper_nouns = load('proper_nouns')
    self.analyzer = Analyzer(self.prefixes, self.suffixes, self.unvoweled_nouns, 
                             self.unvoweled_verbs, self.tool_words, self.proper_nouns)

class TestCheckToolWords(TestAnalyzer):
  def test_match(self):
    self.analyzer.stem = u'على'
    tool_word = self.analyzer.check_tool_words()
    self.assertEqual(tool_word.unvoweled_form, u'على')

  def test_mismatch(self):
    self.analyzer.stem = u'يعلو'
    tool_word = self.analyzer.check_tool_words()
    self.assertIsNone(tool_word)

class TestCheckProperNouns(TestAnalyzer):
  def test_match(self):
    self.analyzer.stem = u'كريم'
    proper_noun = self.analyzer.check_proper_nouns()
    self.assertEqual(proper_noun.unvoweled_form, u'كريم')

  def test_mismatch(self):
    self.analyzer.stem = u'كبير'
    proper_noun = self.analyzer.check_proper_nouns()
    self.assertIsNone(proper_noun)

class TestFindRegexAndRoots(TestAnalyzer):
  '''
  find_regex_and_roots should return the corresponding regex pf pattern
  and the possible roots even if a mismatch occurs
  '''
  def setUp(self):
    super(TestFindRegexAndRoots, self).setUp()
    self.pattern = self.unvoweled_nouns[4][1]
    self.length = 4

  def test_mismatch(self):
    self.analyzer.stem = u'لعبة'
    regex, roots = self.analyzer.find_regex_and_roots(self.pattern, self.length)
    self.assertEqual(regex.encode('utf8'), r'^آ.ا.$')
    self.assertIn(u'ءعة', roots)

  def test_match(self):
    self.analyzer.stem = u'آثار'
    regex, roots = self.analyzer.find_regex_and_roots(self.pattern, self.length)
    self.assertEqual(regex.encode('utf8'), r'^آ.ا.$')
    self.assertIn(u'ءثر', roots)

  def test_special_case(self):
    self.analyzer.stem = u'رأيت'
    self.pattern = self.unvoweled_verbs[4][68]
    regex, roots = self.analyzer.find_regex_and_roots(self.pattern, self.length)
    self.assertEqual(regex.encode('utf8'), r'^...ت$') 
    self.assertIn(u'رأي', roots)

class TestFindInNouns(TestAnalyzer):
  def setUp(self):
    super(TestFindInNouns, self).setUp()
    self.length = 4
    self.patterns = self.unvoweled_nouns[4]

  def test_noun(self):
    self.analyzer.stem = u'آثار'
    roots = self.analyzer.find_in(self.patterns)
    self.assertIn(u'ءثر', roots)

  def test_second_nouns(self):
    self.analyzer.stem = u'لعبة'
    roots = self.analyzer.find_in(self.patterns)
    self.assertIn(u'لعب', roots)

class TestFindInVerbs(TestAnalyzer):
  def setUp(self):
    super(TestFindInVerbs, self).setUp()
    self.length = 6
    self.patterns = self.unvoweled_verbs[6]

  def test_verb(self):
    self.analyzer.stem = u'يلعبون'
    roots = self.analyzer.find_in(self.patterns)
    self.assertIn(u'لعب', roots)

  def test_second_verb(self):
    self.analyzer.stem = u'يزمجرن'
    roots = self.analyzer.find_in(self.patterns)
    self.assertIn(u'زمجر', roots)

class TestFindRootNoun(TestAnalyzer):
  def test_with_common_prefix_and_suffix(self):
    self.analyzer.prefix = self.prefixes[1] # Waw Al-Atf
    self.analyzer.suffix = self.suffixes[1] # Kaf Al-Mokhatab
    self.analyzer.stem = u'كتاب'
    roots = self.analyzer.find_root()
    self.assertIn(u'كتب', roots)

# NEXT STEP:
## COMPARE found roots to root store, filter using rules
if __name__ == '__main__':
  unittest.main()