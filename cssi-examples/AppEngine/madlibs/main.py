# main.py
# the import section

import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class CollectInfo(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/collect_form.html")
        self.response.write(template.render())

class Story(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("templates/story.html")
        protagonist = self.request.get("protagonist")
        event = self.request.get("event")
        pluralNoun = self.request.get("pluralNoun")
        name = self.request.get("name")
        skill = self.request.get("skill")
        number = self.request.get("number")
        largerNumber = self.request.get("largerNumber")
        answer = float(number) / float(largerNumber) * 100
        adjective = self.request.get("adjective")
        place = self.request.get("place")
        templateVars = {
            "protagonist": protagonist,
            "event": event,
            "pluralNoun": pluralNoun,
            "name": name,
            "skill": skill,
            "number": number,
            "largerNumber": largerNumber,
            "answer": answer,
            "adjective": adjective,
            "place": place,
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", CollectInfo),
    ("/story", Story),
], debug=True)
