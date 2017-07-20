
import jinja_env
import logging
import webapp2
import os
#from [folder] import [filename]
from models import user_model

from google.appengine.ext import ndb
from google.appengine.api import users 


class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "College Ebay",
            "html_login_url": users.create_login_url("/listing"),
        }
        template = jinja_env.env.get_template('templates/maintmpl.html')
        self.response.out.write(template.render(html_params))


                
                
                