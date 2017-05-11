from google.appengine.ext import db
from models.user import User
from models.post import Post
import webapp2
import os
from handlers.handler import Handler
from main import jinja_env
from main import template_dir

# Function for adding a new Post to the datastore


class NewPostHandler(Handler):
    def render_front(self, subject="", content="", error=""):
        blogs = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
        self.render("new_post.html", subject=subject, content=content,
                    error=error, blogs=blogs)

    def get(self):
        if self.user:
            self.render_front()
        else:
            self.redirect('/login')

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            b = Post(parent=blog_key(), subject=subject, content=content,
                     author=self.user.name)
            b.put()
            self.redirect('/blog/%s' % str(b.key().id()))
        else:
            error = "We need both a subject and some content"
            self.render_front(subject, content, error)

# Function for displaying the new blog added by the user


class LinkHandler(Handler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        blog = db.get(key)
        if not blog:
            self.error(404)
            return
        self.render("new_blog.html", blog=blog)
