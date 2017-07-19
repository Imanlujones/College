
import jinja_env
import logging
import webapp2

# from [folder] import [filename]
from models import sales_model

from google.appengine.ext import ndb
from google.appengine.api import users


class SalesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.env.get_template('/templates/sales.html')
        logging.info("MainHandler")
        logging.info(users.get_current_user())
        logging.info(users.create_login_url("/profile"))

        current_user = users.get_current_user()

        html_params = {
            "title": "Profile",
        }
        user = users.get_current_user()
        if user != None:
            html_params["html_user"] = user.email()
        self.response.out.write(template.render(html_params))


    def post(self):
        logging.info("USER SAID POST")
        r_item = self.request.get("form_item")
        r_url = self.request.get("form_url")
        r_category = self.request.get("form_category")
        r_personnumber = self.request.get("form_number")
        r_price = self.request.get("form_price")

        logging.info(r_item)
        logging.info(r_url)
        logging.info(r_category)
        logging.info(r_personnumber)
        logging.info(r_price)

        new_item = sales_model.SalesModel(
                item_name=r_item,
                pic_url=r_url,
                category_name=r_category,
                person_number=r_personnumber,
                price_amount=r_price
            )
        new_item.put()
        template = jinja_env.env.get_template('/templates/sale_2.0.html')
        logging.info("Saleshandler")
        sales_info = {
            "Item":r_item,
            "Category":r_category,
            "Picture":r_url,
            "Price":r_price,
        }
        self.response.out.write(template.render(sales_info))
