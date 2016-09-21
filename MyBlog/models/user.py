from google.appengine.ext import db
import string
import hashlib
import hmac
import random

# Password hashing functions


def make_salt(length=5):
    return ''.join(random.choice(string.letters) for x in xrange(length))


def make_pw_hash(name, pw, salt=None):
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

# The function valid_pw() returns True if a user's password
# matches its hash.


def valid_pw(name, pw, h):
    salt = h.split(',')[1]
    n_h = make_pw_hash(name, pw, salt)
    return n_h == h

# Defines a parent for the User


def users_key(group='default'):
    return db.Key.from_path('users', group)

# Create the model for User entity


class User(db.Model):
    name = db.StringProperty(required=True)
    pw_hash = db.StringProperty(required=True)
    email = db.StringProperty()

    @classmethod
    def by_id(cls, uid):
        return cls.get_by_id(uid, parent=users_key())

    @classmethod
    def by_name(cls, name):
        u = cls.all().filter('name =', name).get()
        return u

    @classmethod
    def register(cls, name, pw, email=None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent=users_key(), name=name, pw_hash=pw_hash,
                    email=email)

    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
