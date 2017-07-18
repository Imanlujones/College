import os
import webapp2

from handlers import jinja_env
from handlers import main_handler
from handlers import second_handler
from handlers import createprofile_handler
from handlers import third_handler
from handlers import fourth_handler

jinja_env.init(os.path.dirname(__file__))

app = webapp2.WSGIApplication([
    ('/', main_handler.MainHandler),
    ('/second', second_handler.SecondHandler),
    ('/createprofile', createprofile_handler.CreateProfileHandler),
    ('/profile', third_handler.ThirdHandler), 
    ('/sales', fourth_handler.FourthHandler),
], debug=True)
