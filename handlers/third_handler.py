
import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users


class ThirdHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.env.get_template('/templates/profile.html')
        logging.info("MainHandler")
        html_params = {
            "title": "Profile",
            "content": "Hello"
        }
        self.response.out.write(template.render(html_params))