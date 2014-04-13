# -*- coding: UTF-8 -*-

import re, itertools, booby, codecs, datrie, pdb
from booby import Model, fields, serialize
from db.booby_models.booby_models import *
from utils import ARABIC_CHARS, DB_PATH

OUTFILE = "/home/karim/monakeb/matches.txt"

WORD = u'الحب'
# انفتاح

def __main__():
    word = WORD
    exceptional_words = load('exceptional_words')
    exceptional = check_exceptional(word, exceptional_words)  # Check if Lafz Al-Galala
    if exceptional:
        print word
        return word
    prefixes = load('prefixes')
    suffixes = load('suffixes_reversed')
    unvoweled_nouns = load_patterns('nouns/unvoweled/unvoweled_nominal_patterns')
    unvoweled_verbs = load_patterns('verbs/unvoweled/unvoweled_verbal_patterns')
    tool_words = load('tool_words')
    proper_nouns = load('proper_nouns')
    roots = load_roots()
    seg = Segmentor(word, prefixes, suffixes)
    matches = seg.split_string()
    analyzer = Analyzer(prefixes, suffixes, unvoweled_nouns, unvoweled_verbs,
                        tool_words, proper_nouns, roots)
    possible_roots = set()
    for match in matches:
        analyzer.prefix, analyzer.stem, analyzer.suffix = match
        roots = analyzer.find_root()
        for root in roots:
            possible_roots.add(root)
    
    for root in possible_roots:
        print root
        # return roots


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

def check_exceptional(word, exceptional_words):
    for pattern in exceptional_words:
        if pattern.unvoweled_form == word:
            return pattern.stem

def load_roots():
    roots = set()
    with codecs.open(DB_PATH + 'roots.txt', 'r', 'utf8') as f:
        for line in f:
            if not line.isspace():
                line = line.strip()
                roots.add(line)
    return roots

class Segmentor:
    def __init__(self, string, prefix_list, suffix_list):
        self.string = string
        self.prefix_list = prefix_list
        self.suffix_list = suffix_list

    def setup_prefixes(self):
        ''' returns a Trie of all prefixes '''
        prefixes = datrie.Trie(ARABIC_CHARS)
        seen_prefixes = set()
        for prefix in self.prefix_list:
            unvoweled = prefix.unvoweled_form
            if unvoweled not in seen_prefixes:
                seen_prefixes.add(unvoweled)
                prefixes[unvoweled] = [prefix]
            else:
                prefixes[unvoweled].append(prefix)
        return prefixes

    def setup_suffixes(self):
        '''returns a Trie of all suffixes reversed '''
        suffixes = datrie.Trie(ARABIC_CHARS)
        seen_suffixes = set()
        for suffix in self.suffix_list:
            unvoweled = suffix.unvoweled_form
            if unvoweled not in seen_suffixes:
                seen_suffixes.add(unvoweled)
                suffixes[unvoweled] = [suffix]
            else:
                suffixes[unvoweled].append(suffix)
        return suffixes

    def match_prefix(self, word, prefix_trie):
        '''
        returns all prefix matches form prefix_trie to word
        '''
        return prefix_trie.prefix_items(word)


    def match_suffix(self, word, suffix_trie):
        '''
        returns all suffix matches form suffix_trie to word
        '''
        return suffix_trie.prefix_items(word[::-1])

    def reverse_suffix(self, suffix):
        '''
        modifies the suffix in place by reversing its 
        unvoweled and voweled forms
        '''
        suffix.unvoweled_form = suffix.unvoweled_form[::-1]
        suffix.voweled_form = suffix.voweled_form[::-1]

    def find_combinations(self, prefixes, suffixes):
        '''
        Generates tuples of all possible
        (prefix, stem, suffix) combinations
        '''
        empty_prefix = self.prefix_list[0]
        empty_suffix = self.suffix_list[0]
        match = (empty_prefix, self.string, empty_suffix) # no prefix or suffix
        res = self.filter(match)
        if res:
            yield res
        # prefix only
        for prefix_str, prefix_objects in prefixes:
            for prefix in prefix_objects:
                match = (prefix, self.string[len(prefix_str):], empty_suffix)
                res = self.filter(match)
                if res:
                    yield res
        # suffix only
        for suffix_str, suffix_objects in suffixes:
            for suffix in suffix_objects:
                self.reverse_suffix(suffix)
                suffix_str = suffix.unvoweled_form
                match = (empty_prefix, self.string[:-len(suffix_str)], suffix)
                res = self.filter(match)
                if res:
                    yield res
        # prefix and suffix
        for (prefix_str, prefix_objects), (suffix_str, suffix_objects) in \
        itertools.product(prefixes, suffixes):
            # note that suffix is in normal order here
            for prefix in prefix_objects:
                for suffix in suffix_objects:
                    # suffix_str = suffix.unvoweled_form  # this is reversed order  
                    stem = self.string[len(prefix_str):-len(suffix_str)]
                    match = (prefix, stem, suffix)
                    res = self.filter(match)
                    if res:
                        yield res

    def filter(self, match):
        '''
        Gnereates filtered tuples of matches
        based on Arabic language rules
        '''
        prefix, stem, suffix = match
        suffix_length = len(suffix.unvoweled_form)
        if (prefix.p_class[0] == "N" and suffix.s_class[0] == "V") \
        or (prefix.p_class[0] == "V" and suffix.s_class[0] == "N")  \
        or (len(stem) < 2 or len(stem) > 9) \
        or (prefix.p_class in ["N1", "N2", "N3", "N5"] and suffix_length != 0):
            return
        else:
            return (prefix, stem, suffix)

    def split_string(self):
        '''
        returns all possible combinations of prefix, stem, suffix 
        that match self.string 
        '''
        prefix_trie = self.setup_prefixes()
        suffix_trie = self.setup_suffixes()
        matched_prefixes= self.match_prefix(self.string, prefix_trie)        
        matched_suffixes= self.match_suffix(self.string, suffix_trie)
        combinations= self.find_combinations(matched_prefixes, matched_suffixes)
        return combinations

class Analyzer:
    def __init__(self, prefixes, suffixes, unvoweled_nouns,
                 unvoweled_verbs, tool_words, proper_nouns, roots):
        self.prefixes = prefixes
        self.suffixes = suffixes
        self.unvoweled_nouns = unvoweled_nouns
        self.unvoweled_verbs = unvoweled_verbs
        self.tool_words = tool_words
        self.proper_nouns = proper_nouns
        self.prefix, self.stem, self.suffix = "", "", ""
        self.dict_roots = roots

    def check_tool_words(self):
        for tool_word in self.tool_words:
            if tool_word.unvoweled_form == self.stem:
                return tool_word

    def check_proper_nouns(self):
        for proper_noun in self.proper_nouns:
            if proper_noun.unvoweled_form == self.stem:
                return proper_noun

    def find_root(self):
        tool_word = self.check_tool_words()
        res = []
        if tool_word:
            return normalize_hamza([tool_word.unvoweled_form])
        proper_noun = self.check_proper_nouns()
        if proper_noun:
            res.extend(normalize_hamza([proper_noun.unvoweled_form]))
        length = len(self.stem)
        if self.prefix.p_class[0] == "N" or self.suffix.s_class[0] == "N":
            roots = self.find_in(self.unvoweled_nouns[length])
        elif self.prefix.p_class[0] == "V" or self.suffix.s_class[0] == "V":
            roots = self.find_in(self.unvoweled_verbs[length])
        else:
            roots = self.find_in(self.unvoweled_nouns[length] + self.unvoweled_verbs[length])
        normalized = normalize_hamza(roots)
        res.extend(self.check_dictionary(normalized))
        return res

    def find_in(self, patterns):
        possible_roots = []
        for pattern in patterns:
            regex = self.get_regex(pattern)
            if re.match(regex, self.stem):
                roots = self.get_roots_from_pattern(pattern)
                # print "Pattern:", pattern.value, "regex:", regex, "stem", self.stem
                possible_roots.extend(roots)
        return possible_roots

    def get_regex(self, pattern):
        regex = u''
        for char in pattern.value:
            if char in [u'ف', u'ع', u'ل']:
                regex += u'.'
            else:
                regex += char
        regex = r'^%s$' %regex
        return regex

    def get_roots_from_pattern(self, pattern):
        roots = []
        possible_rules = pattern.rules.split()
        for rule in possible_rules:
            root = ''
            for char in rule:
                if char.isdigit():
                    index = int(char)
                    root += self.stem[index-1]
                else:
                    root += char
            roots.append(root)
        return roots

    def check_dictionary(self, roots):
        checked = set()
        for root in roots:
            if root in self.dict_roots:
                checked.add(root)
        return checked

def normalize_hamza(roots):
    normalized = []
    hamzas_translation = dict((ord(char), ord(u'ء')) for char in u'أإؤئ')
    hamzas_translation[ord(u'ى')] = ord(u'ا')
    for root in roots:
        normalized.append(root.translate(hamzas_translation))
    return normalized


if __name__ == "__main__":
    __main__()