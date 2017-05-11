# Multi User Blog Website

The Multi User Blog Website provides an interface for the users to view, create, edit, delete blog posts and also to like/ unlike 
posts or comment on posts. The blog application is built using HTML, Python, Google App Engine and Jinja2 template library.
You can access the blog using the url fsndblog.appspot.com/blog

### User Interface

The Blog Website has a front page that lists blog posts. A user can create or modify posts only if they login.
The front page has the option for a user to login or a new user to signup.
Once logged in a user can: 
View the posts 
Create new posts. Creating a new post takes them to new Blog's page.
Edit posts 
Delete posts (Users can only edit/delete their posts.)
Like / Unlike posts only once but not their own.They receive an error message if they disobey this rule.
Comment on posts.
Edit / Delete comments. They can only edit/delete their own comments.

### Quick Start

The following quick start options are available:

- Download the lastest release.
- Clone the repo: git clone https://github.com/pribala/udacity_projects.git.
- To access the blog use the url fsndblog.appspot.com/blog. From there you can navigate to the login and signup page.
- This page lists all the blogs created. To edit the blog posts you need to signup/ login.

### What's Included

Within the repo you'll find the following directories and files:

udacity_projects
  * MyBlog 
      * static
		* framework.css
		* main.css
      * templates
		* base.html
        * front.html
        * welcome.html
        * new_post.html
		* new_blog.html
		* edit-post.html
		* delete-post.html
		* like-post.html
		* unlike-post.html
		* login_user.html
		* signup_page.html
		* new-comment.html
		* comment.html
		* edit-comment.html
		* delete-comment.html
	  * main.py
      * models
        * user.py
        * post.py
        * comment.py		
      * readme.md 
      * app.yaml
	  
### Requirements

Install Python if it is not already installed on the system.
This site uses google app engine to serve the content of the site.


### Reference:
  * http://www.w3schools.com/ for HTML, CSS reference  
  * The Google App Engine documentation https://cloud.google.com/appengine/docs/python/
  * Jinja2 template library documentation http://jinja.pocoo.org/docs/dev/  
  * http://www.tutorialspoint.com/python/ for working with datetime variables 

