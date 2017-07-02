import booby, codecs
from booby import Model, fields, serialize

class Base(Model):
	meta = {'allow_serialize': True}

class PrefixB(Base):
	unvoweled_form = fields.String()
	voweled_form = fields.String()
	description = fields.String()
	p_class = fields.String()

class SuffixB(Base):
	unvoweled_form = fields.String()
	voweled_form = fields.String()
	description = fields.String()
	s_class = fields.String()

# Special Words
class ExceptionalWordB(Base):
	unvoweled_form = fields.String()
	voweled_form = fields.String()
	prefix = fields.String()
	stem = fields.String()
	word_type = fields.String()
	suffix = fields.String()

class ProperNounB(Base):
	unvoweled_form = fields.String()
	voweled_form = fields.String()
	noun_type = fields.String()

class ToolWordB(Base):
	unvoweled_form = fields.String()
	voweled_form = fields.String()
	word_type = fields.String()
	prefix_class = fields.String()
	suffix_class = fields.String()
	priority = fields.String()


# Nouns
class UnvoweledNominalPatternB(Base):
	value = fields.String()
	rules = fields.String()
	ids = fields.String()
	pat_num = fields.Integer()


class VoweledNominalPatternB(Base):
	pat_id = fields.String()
	diac = fields.String()
	canonic = fields.String()
	pat_type =fields.String()
	cas = fields.String()
	ncg = fields.String()
	pat_num = fields.Integer()


# Verbs
class UnvoweledVerbalPatternB(Base):
	value = fields.String()
	rules = fields.String()
	ids = fields.String()
	pat_num = fields.Integer()

class VoweledVerbalPatternB(Base):
	pat_id = fields.String()
	diac = fields.String()
	canonic = fields.String()
	pat_type = fields.String()
	pat_num = fields.Integer()
	aug = fields.String()
	cas = fields.String()
	ncg = fields.String()
	trans = fields.String()

class NominalRootB(Base):
	value = fields.String()
	vect = fields.String()
	root_type = fields.Integer()
	char = fields.String()

class VerbalRootB(Base):
	value = fields.String()
	vect = fields.String()
	root_type = fields.Integer()
	char = fields.String()