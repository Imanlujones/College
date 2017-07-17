
import jinja_env
import logging
import webapp2


class LoginHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/login"))

        dictionary = {
                
                "html_login_url": users.create_login_url("/login"),
            }

        template = jinja_env.env.get_template('templates/logintmpl.html')
        self.response.out.write(template.render(dictionary))

            #dictionary["html_user"] = current_user.email()