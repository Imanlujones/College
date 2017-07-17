
import jinja_env
import logging
import webapp2
#from [folder] import [filename]
from models import user_model


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

        new_user_var = user_model.UserModel(
            user_name = r_name,
            form_classification = r_classification, 
            user_email = "FIX ME LATER",
        )

        new_user_var.put()
        self.redirect("/")
        #redirecrt them to any page on the website (that's what the / is)
            #dictionary["html_user"] = current_user.email()