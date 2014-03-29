from base_model import *

class UnvoweledNominalPattern(BaseModel):
	value = CharField()
	rules = CharField()
	pat_num = IntegerField()
	ids = TextField()

class VoweledNominalPattern(BaseModel):
	pat_id = TextField()
	diac = TextField()
	canonic = TextField()
	pat_type = CharField()
	pat_num = IntegerField() 
	cas = CharField()
	ncg = CharField()

class NominalRoot(BaseModel):
	value = CharField()
	vect = TextField()
	root_type = IntegerField()
	char = CharField()
