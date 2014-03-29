# if __name__ == "__main__" and __package__ is None:
#     __package__ = "PyKhalil-lib.db.migrations.create_tables"

from peewee import *
from ..nouns import *
from ..verbs import *
from ..prefixes import *
from ..suffixes import *
from ..special_words import *

my_db.connect()

# UnvoweledNominalPattern.create_table()
# VoweledNominalPattern.create_table()
# NominalRoot.create_table()
# UnvoweledVerbalPattern.create_table()
# VoweledVerbalPattern.create_table()
# VerbalRoot.create_table()
# Prefix.create_table()
# Suffix.create_table()
# ExceptionalWord.create_table()
# ProperNoun.create_table()
# ToolWord.create_table()

print 'Success !'