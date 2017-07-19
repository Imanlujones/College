
import jinja_env
import logging
import webapp2
from models import sales_model
from handlers import sales_handler


class listingHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("listingHandler")
        new_items = sales_model.SalesModel.query(sales_model.SalesModel.category_name==self.request.get("type")).fetch()
        sales_str = ""

        logging.info("numberofitemsis" + (str(len(new_items))))




        for sales in new_items:
            sales_str += "<div>"
            sales_str += "<h2>User : " + "?" + "</h2>"
            sales_str += "<p>" + sales.category_name + "</p>" 
            sales_str += "<p>" + sales.item_name + "</p>"
            sales_str += "<p>Price : " + sales.price_amount + "</p>"
            sales_str += "<p>Contact Info :" + sales.person_number + "</p>"
            sales_str += "<p>" + "<img src='"+sales.pic_url+"'>" + "</p>"
            sales_str += "</div>"
        html_params = {
            "title": "Second Title",
            "content": sales_str,
        }
        template = jinja_env.env.get_template('templates/listing.html')
        self.response.out.write(template.render(html_params))