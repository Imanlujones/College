
import jinja2
import logging
import webapp2
import os
#from [folder] import [filename]
from models import user_model

from google.appengine.ext import ndb
from google.appengine.api import users 

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/login"))

        dictionary = {
                
                "html_login_url": users.create_login_url("/login"),
                }

        template = jinja_env.env.get_template('templates/logintmpl.html')
        self.response.out.write(template.render(dictionary))

    def post(self):
        logging.info("USER SAID POST")
        r_name = self.request.get("form_name")
        r_classification = self.request.get("form_classification")
        r_pic = self.request.get("form_pic")
        r_major = self.request.get ("form_major")
        logging.info(r_name)
        logging.info(r_classification)
        logging.info(r_major)

        new_user_var = user_model.UserModel(
            user_name = r_name,
            form_classification = r_classification, 
            user_email = "FIX ME LATER",
        )

        new_user_var.put()
        template = jinja_env.env.get_template('/templates/sale_2.0.html')
        logging.info("LoginHandler")
        user_info={
            "User":r_name,
            "Classification":r_classification,
            "Major": r_major,
        }
        self.redirect("/listing")
        #redirecrt them to any page on the website (that's what the / is)
            #dictionary["html_user"] = current_user.email()