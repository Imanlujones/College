
import jinja2
import logging
import webapp2
import os
import jinja_env
#from [folder] import [filename]
from models import user_model

from google.appengine.ext import ndb
from google.appengine.api import users 

class CreateProfileHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/createprofile"))

        dictionary = {
                
                "html_login_url": users.create_login_url("/createprofile"),
                }

        template = jinja_env.env.get_template('templates/createprofile.html')
        self.response.out.write(template.render(dictionary))

    def post(self):
        logging.info("USER SAID POST")
        r_name = self.request.get("form_name")
        r_classification = self.request.get("form_classification")
        r_pic = self.request.get("form_pic")
        r_major = self.request.get ("form_major")

        new_user_var = user_model.UserModel(
            user_name = r_name,
            form_classification = r_classification, 
            user_email = "FIX ME LATER",
        )

        new_user_var.put()
        self.redirect("/profile")
        #redirecrt them to any page on the website (that's what the / is)
            #dictionary["html_user"] = current_user.email()