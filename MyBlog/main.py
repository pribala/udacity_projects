#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import cgi
import re
import random
import string
import hashlib
import hmac
from google.appengine.ext import db
import urlparse
from models.user import User
from models.post import Post
from models.post import blog_key
from models.comment import Comment


# initializing the template library
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)

secret = "du.uyX9fE~Tb6.pp&U3D-0smY0,Gqi$^jS34tju9"

# Hashing functions

# Create a secure cookie value


def make_secure_val(val):
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

# Check the validity of the user cookie


def check_secure_val(secure_val):
    val = secure_val.split("|")[0]
    if secure_val == make_secure_val(val):
        return val

# User Input Authentication code


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")

# Min 3 chars and max 20


PASS_RE = re.compile(r"^.{3,20}$")

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

# Checking for valid username value


def valid_username(username):
    return username and USER_RE.match(username)

# Checking for valid email value


def valid_email(email):
    return not email or EMAIL_RE.match(email)

# Checking for valid password value


def valid_password(password):
    return password and PASS_RE.match(password)


# Handler functions for rendering, initializing, login, logout


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header('Set-Cookie', '%s=%s; Path=/'
                                         % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)

    def login(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))

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

# User signup code


class SignUpHandler(Handler):
    def get(self):
        self.render("signup_page.html")

    def post(self):
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')
        params = dict(username=self.username, email=self.email)
        if not valid_username(self.username):
            params['error1'] = "Enter a valid username"
            have_error = True
        if not valid_password(self.password):
            params['error2'] = "Enter a valid password"
            have_error = True
        elif self.password != self.verify:
            params['error3'] = "The passwords don't match"
            have_error = True
        if not valid_email(self.email):
            params['error4'] = "Enter a valid email"
            have_error = True
        if have_error:
            self.render("signup_page.html", **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError

# Checks if user already exists else creates a new user


class Register(SignUpHandler):
    def done(self):
        u = User.by_name(self.username)
        if u:
            msg = " The user already exists"
            self.render('signup_page.html', error1=msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()
            self.login(u)
            self.redirect('/welcome')

# Logged in users can access the Post dashboard


class WelcomeHandler(Handler):
    def get(self):
        if self.user:
            blogs = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 10")  # noqa
            self.render("welcome.html", username=self.user.name, blogs=blogs)
        else:
            self.redirect('/login')

# Checks if user exists and logs them in


class LoginHandler(Handler):
    def get(self):
        self.render("login_user.html")

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/welcome')
        else:
            msg = "Invalid login.Please enter a valid username and password or go to the signup page"  # noqa
            self.render("login_user.html", error=msg)

# Logs out the user


class Logout(Handler):
    def get(self):
        if self.user:
            self.logout()
            self.redirect('/login')

# Delete function displays all the posts by the logged in user and
# deletes the selected posts


class DeletePost(Handler):
    def get(self):
        if self.user:
            username = self.user.name
            blogs = db.GqlQuery("SELECT * FROM Post WHERE author ='" + username + "'")  # noqa
            error = ""
            self.render("delete-post.html", blogs=blogs, error=error)

    def post(self):
        blogid = self.request.get_all('delete-post')
        for bid in blogid:
            postid = int(bid)
            b = Post.by_id(postid)
            if b.author == self.user.name:
                b.delete()
            else:
                error = "You can only delete blogs you created!"
                self.render("delete-post.html", error=error)
        self.redirect('/welcome')

# Allows logged in user to edit their posts


class EditPost(Handler):
    def render_front(self, subject="", content="", error=""):
        self.render("edit-post.html", subject=subject, content=content,
                    error=error)

    def get(self, post_id):
        if self.user:
            postid = int(post_id)
            blog = Post.by_id(postid)
            if not blog:
                self.error(404)
                return
            username = self.user.name
            if blog.author == username:
                self.render_front(blog.subject, blog.content)
            else:
                error = "You can only blogs created by you!"
                self.render_front(error=error)
        else:
            self.redirect('/login')

    def post(self, post_id):
        subject = self.request.get('subject')
        content = self.request.get('content')
        if subject and content:
            postid = int(post_id)
            b = Post.by_id(postid)
            if b.author == self.user.name:
                b.subject = subject
                b.content = content
                b.author = self.user.name
                b.put()
                self.redirect('/blog/%s' % str(b.key().id()))
            else:
                error = "You can only edit blogs created by you"
                self.render_front(error=error)
        else:
            error = "We need both a subject and some content"
            self.render_front(subject, content, error)

# User can un-like posts created by others but only once


class UnlikePost(Handler):
    def get(self, post_id):
        if self.user:
            postid = int(post_id)
            blog = Post.by_id(postid)
            if blog.author != self.user.name:
                error = ""
                self.render("unlike-post.html", blog=blog, error=error)
            else:
                error = "You cannot Like/Unlike your own posts!"
                self.render("unlike-post.html", blog=blog, error=error)
        else:
            self.redirect('/login')

    def post(self, post_id):
        postid = int(post_id)
        blog = Post.by_id(postid)
        error = ""
        if self.user.name != blog.author:
            if self.user.name in blog.dislikes_post:
                error = "You have already Un-liked this Post!"
                self.render("unlike-post.html", blog=blog, error=error)
            elif self.user.name in blog.likes_post:
                error = "You have already Liked this Post!"
                self.render("unlike-post.html", blog=blog, error=error)
            else:
                blog.dislikes_post.append(self.user.name)
                blog.put()
                self.redirect('/welcome')

# User can like a post created by others but only once


class LikePostHandler(Handler):
    def get(self, post_id):
        if self.user:
            postid = int(post_id)
            blog = Post.by_id(postid)
            if blog.author != self.user.name:
                error = ""
                self.render("like-post.html", blog=blog, error=error)
            else:
                error = "You cannot Like/Unlike your own posts!"
                self.render("like-post.html", blog=blog, error=error)
        else:
            self.redirect('/login')

    def post(self, post_id):
        postid = int(post_id)
        blog = Post.by_id(postid)
        error = ""
        if self.user.name != blog.author:
            if self.user.name in blog.likes_post:
                error = "You have already Liked this Post!"
                self.render("like-post.html", blog=blog, error=error)
            elif self.user.name in blog.dislikes_post:
                error = "You have already Un-Liked this Post!"
                self.render("like-post.html", blog=blog, error=error)
            else:
                blog.likes_post.append(self.user.name)
                blog.put()
                self.redirect('/welcome')

# Function for creating a new comment for a post
# Only logged in users can create a comment


class NewCommentHandler(Handler):
    def render_front(self, content="", error="", title=""):
        comments = db.GqlQuery("SELECT * FROM Comment ORDER BY created DESC")
        self.render("new-comment.html", content=content, error=error,
                    title=title, comments=comments)

    def get(self, post_id):
        if self.user:
            postid = int(post_id)
            blog = Post.by_id(postid)
            title = blog.subject
            self.render_front(title=title)
        else:
            self.redirect('/login')

    def post(self, post_id):
        if self.user:
            content = self.request.get('content')
            postid = int(post_id)
            blog = Post.by_id(postid)
            title = blog.subject
            if content:
                comment = Comment(title=title, content=content,
                                  created_by=self.user.name, post_id=postid)
                comment.put()
                self.redirect('/comment')
            else:
                error = "We need some content for the comment"
                self.render_front(title, content, error)
        else:
            self.redirect('/login')

# Function renders the comments from the datastore
# Only logged in users can see the comments


class CommentHandler(Handler):
    def get(self):
        comments = db.GqlQuery("SELECT * FROM Comment ORDER BY date_created DESC LIMIT 10")  # noqa
        if self.user:
            self.render("comment.html", username=self.user.name,
                        comments=comments)
        else:
            self.redirect('/login')

# Function for editing an existing comment
# Only logged in users can edit comments
# Users can only edit comments posted by them


class EditCommentHandler(Handler):
    def render_front(self, title="", content="", error=""):
        self.render("edit-comment.html", title=title, content=content,
                    error=error)

    def get(self, comment_id):
        if self.user:
            commentid = int(comment_id)
            comment = Comment.by_id(commentid)
            if not comment:
                self.error(404)
                return
            if self.user.name == comment.created_by:
                self.render_front(comment.title, comment.content)
            else:
                error = "You can only edit comments you created"
                self.render_front(error=error)
        else:
            self.redirect('/login')

    def post(self, comment_id):
        content = self.request.get('content')
        commentid = int(comment_id)
        comment = Comment.by_id(commentid)
        if self.user.name == comment.created_by:
            if content:
                comment.title = comment.title
                comment.post_id = comment.post_id
                comment.content = content
                comment.created_by = self.user.name
                comment.put()
                self.redirect('/comment')
            else:
                error = "We need some content for the comment"
                self.render_front(title, content, error)
        else:
            error = "You can only edit comments you created."
            self.render_front(error)

# Function for deletion of a comment
# Only logged in users can delete comments
# Users can only delete their own comments


class DeleteComment(Handler):
    def get(self, comment_id):
        if self.user:
            commentid = int(comment_id)
            comment = Comment.by_id(commentid)
            if comment.created_by == self.user.name:
                error = ""
                self.render("delete-comment.html", comment=comment,
                            error=error)
            else:
                error = "You can only delete comments created by you!"
                self.render("delete-comment.html", comment=comment,
                            error=error)
        else:
            self.redirect('/login')

    def post(self, comment_id):
        if self.user:
            username = self.user.name
            commentid = int(comment_id)
            comment = Comment.by_id(commentid)
            if comment.created_by == username:
                comment.delete()
                self.redirect('/comment')
            else:
                error = "You can only delete comments created by you"
                self.render("delete-comment.html", comment=comment,
                            error=error)
        else:
            self.redirect('/login')

# Sets the user cookie to null so only logged in users can edit posts
# Renders the last 10 posts from the datastore


class MainHandler(Handler):
    def get(self):
        self.logout()
        blogs = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 10")  # noqa
        self.render("front.html", blogs=blogs)

app = webapp2.WSGIApplication([
    ('/blog', MainHandler),
    ('/blog/newpost', NewPostHandler),
    ('/blog/([0-9]+)', LinkHandler),
    ('/signup', Register),
    ('/welcome', WelcomeHandler),
    ('/login', LoginHandler),
    ('/logout', Logout),
    ('/delete', DeletePost),
    ('/edit/([0-9]+)', EditPost),
    ('/likepost/([0-9]+)', LikePostHandler),
    ('/unlikepost/([0-9]+)', UnlikePost),
    ('/newcomment/([0-9]+)', NewCommentHandler),
    ('/comment', CommentHandler),
    ('/editcomment/([0-9]+)', EditCommentHandler),
    ('/deletecomment/([0-9]+)', DeleteComment),
    ], debug=True)
