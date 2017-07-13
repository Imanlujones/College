
import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users

class ThirdHandler(webapp2.RequestHandler):
	def get(self):
		logging.info("MainHandler")
        html_params = {
            "title": "Profile",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('/templates/profile.html')
        self.response.out.write(template.render(html_params))