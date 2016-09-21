from google.appengine.ext import db

# defines a parent for the blog


def blog_key(name='default'):
    return db.Key.from_path('blogs', name)

# Create the model for Post entity


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    author = db.StringProperty()
    date_modified = db.DateTimeProperty(auto_now=True)
    likes_post = db.StringListProperty()
    dislikes_post = db.StringListProperty()

    @classmethod
    def by_id(cls, pid):
        return cls.get_by_id(pid, parent=blog_key())
