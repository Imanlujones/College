import jinja_env
import logging
import webapp2

# from [folder] import [filename]
from models import sales_model

from google.appengine.ext import ndb
from google.appengine.api import users

class AboutHandler(webapp2.RequestHandler):
    def get(self):
    	logging.info("about_handler")
    	logging.info("about page")
    	html_params = {
    		"Title":"About Us",
    	}
        template = jinja_env.env.get_template('templates/about.html')
        self.response.out.write(template.render(html_params))
