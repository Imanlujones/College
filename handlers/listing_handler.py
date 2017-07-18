
import jinja_env
import logging
import webapp2
from models import sales_model

from models import book

class listingHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("listingHandler")
        new_items = sales_model.SalesModel.query(sales_model.SalesModel.category_name==self.request.get("type")).fetch()
        # do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/listing.html')
        self.response.out.write(template.render(html_params))