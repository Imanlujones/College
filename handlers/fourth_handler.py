
import jinja_env
import logging
import webapp2

# from [folder] import [filename]
from models import sales_model

from google.appengine.ext import ndb
from google.appengine.api import users



class FourthHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.env.get_template('/templates/sales.html')
        logging.info("MainHandler")
        html_params = {
            "title": "Profile",
            "content": "Hello"
        }
        self.response.out.write(template.render(html_params))
    def post(self):
        logging.info("USER SAID POST")
        r_item = self.request.get("form_item")
        r_url = self.request.get("form_url")
        r_category = self.request.get("form_category")
        r_personnumber = self.request.get("form_number")
        r_price = self.request.get("form_price")

        logging.info(r_item)

        new_item = sales_model.SalesModel(
                item_name=r_item,
                pic_url=r_url,
                category_name=r_category,
                number_name=r_personnumber,
                price_amount=r_price
            )

        new_item.put()
        self.redirect("/")

