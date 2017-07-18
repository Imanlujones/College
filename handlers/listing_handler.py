
import jinja_env
import logging
import webapp2

from models import book

class listingHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("listingHandler")
        books = book.Book.query().fetch()
        # do stuff with books...
        html_params = {
            "title": "Second Title",
            "content": ""
        }
        template = jinja_env.env.get_template('templates/listing.html')
        self.response.out.write(template.render(html_params))