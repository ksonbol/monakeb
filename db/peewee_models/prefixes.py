from base_model import *

class Prefix(BaseModel):
	unvoweled_form = CharField()
	voweled_form = CharField()
	description = TextField()
	p_class = CharField()

	def get_class(self):
		return self.p_class
