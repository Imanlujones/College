
import jinja_env
import logging
import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("MainHandler")
        html_params = {
            "title": "College Ebay",
            "content": "Hello"
        }
        template = jinja_env.env.get_template('templates/maintmpl.html')
        self.response.out.write(template.render(html_params))