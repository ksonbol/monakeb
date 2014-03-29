from base_model import *

# my_db = SqliteDatabase('khalil.db')

class ExceptionalWord(BaseModel):
	unvoweled_form = CharField()
	voweled_form = CharField()
	prefix = CharField()
	stem = CharField()
	word_type = TextField()
	suffix = CharField()

class ProperNoun(BaseModel):
	unvoweled_form = CharField()
	voweled_form = CharField()
	noun_type = TextField()

class ToolWord(BaseModel):
	unvoweled_form = CharField()
	voweled_form = CharField()
	word_type = TextField()
	prefix_class = CharField()
	suffix_class = CharField()
	priority = CharField()