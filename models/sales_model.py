from google.appengine.ext import ndb
# Category
# Item
# Link(as a picture)
# Person’s phone number
# # Price

class SalesModel(ndb.Model):
    Category_model = ndb.StringProperty()
    Item_model = ndb.StringProperty()
    pic_url = ndb.StringProperty()
    personmnumber_model = ndb.StringProperty()
    Price_model = ndb.StringProperty()
