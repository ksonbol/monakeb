from base_model import *

class Suffix(BaseModel):
	unvoweled_form = CharField()
	voweled_form = CharField()
	description = TextField()
	s_class = CharField()

	def get_class(self):
		return self.s_class
	