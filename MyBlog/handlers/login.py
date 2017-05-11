from handlers.handler import Handler
from models.user import User
from main import jinja_env
from main import template_dir
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
