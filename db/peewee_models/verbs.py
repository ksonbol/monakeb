from base_model import *

class UnvoweledVerbalPattern(BaseModel):
	value = TextField()
	rules = TextField()
	ids = TextField()
	pat_num = IntegerField()


class VoweledVerbalPattern(BaseModel):
	pat_id = CharField()
	diac = TextField()
	canonic = TextField()
	pat_type = CharField()
	pat_num = IntegerField()
	aug = CharField()
	cas = CharField()
	ncg = CharField()
	trans = CharField()

class VerbalRoot(BaseModel):
	value = CharField()
	vect = TextField()
	root_type = IntegerField()
	char = CharField()