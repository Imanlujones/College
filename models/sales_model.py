from google.appengine.ext import ndb
# Category
# Item
# Link(as a picture)
# Price

class SalesModel(ndb.Model):
    category_name = ndb.StringProperty()
    item_name = ndb.StringProperty()
    pic_url = ndb.StringProperty()
    person_number = ndb.StringProperty()
    price_amount = ndb.StringProperty()
    user_email = ndb.StringProperty()
