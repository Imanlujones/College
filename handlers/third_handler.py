
import jinja_env
import logging
import webapp2

from google.appengine.ext import ndb
from google.appengine.api import users


  template = jinja_env.env.get_template('templates/profile.html')
  self.response.out.write(template.render(html_params))