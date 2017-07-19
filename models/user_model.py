from google.appengine.ext import ndb

class UserModel(ndb.Model):
	user_name = ndb.StringProperty()
	form_classification = ndb.StringProperty()
	user_email = ndb.StringProperty()