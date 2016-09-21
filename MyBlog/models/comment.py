from google.appengine.ext import db

# Create the model for Comment entity


class Comment(db.Model):
    title = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    date_created = db.DateTimeProperty(auto_now_add=True)
    date_modified = db.DateTimeProperty(auto_now=True)
    created_by = db.StringProperty(required=True)
    post_id = db.IntegerProperty(required=True)

    @classmethod
    def by_id(cls, cid):
        return cls.get_by_id(cid)
