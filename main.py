import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import createprofile_handler
from handlers import listing_handler
from handlers import login_handler
from handlers import third_handler
from handlers import sales_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/createprofile', createprofile_handler.CreateProfileHandler),
    ('/listing', listing_handler.listingHandler),
    ('/profile', third_handler.ThirdHandler), 
    ('/sales', sales_handler.SalesHandler),
], debug=True)
