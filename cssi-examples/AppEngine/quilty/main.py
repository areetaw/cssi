import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=["jinja2.ext.autoescape"],
    autoescape=True)

# Handlers
class Patch(ndb.Model):
    inner_color = ndb.StringProperty()
    outer_color = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True) #when new patch, automatically add the create time

class MainPage(webapp2.RequestHandler):
    def get(self):
        patch_query = Patch.query()
        patch_query = patch_query.order(Patch.created_time)
        patches = patch_query.fetch()
        templatesVar = {
            "patches": patches,
        }
        template = env.get_template("templates/quilt.html")
        self.response.write(template.render(templatesVar))

class AddHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/add.html")
        self.response.write(template.render())
    def post(self):
        inner_color = self.request.get("inner_color")
        outer_color = self.request.get("outer_color")
        newPatch = Patch(inner_color=inner_color, outer_color=outer_color)
        newPatch.put()
        self.redirect("/")

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/add", AddHandler),
], debug=True)
