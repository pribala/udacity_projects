# Project: Linux Server Configuration

This project entailed configuring a Linux server to host web applications. 
The server was secured from a number of attack vectors, a database server, PostgreSQL,
was installed and configured, and the web application Item Catalog was deployed onto it.

### Server Access

IP Address: 34.193.246.181

Web Application URL : http://34.193.246.181

DNS Name: http://ec2-107-23-141-18.compute-1.amazonaws.com

Port: 2200

### Project Overview

I configured and secured a new Ubuntu Linux server instance on Amazon Lightsail to host 
a databse server, and a data driven web application. This was accomplished by installing 
Apache2 server to serve Python Flask application that connects to a PostgreSQL database.

### Installed Packages

Package Name | Description
------------ | -----------
finger	| Displays an easy to read information about a user
apache2	| HTTP Server
libapache2-mod-wsgi | Hosts Python applications on Apache2 server
ntp	| Synchronizes time over a network
postgresql | Postgresql Database server
git	| Version control system tools
python-setuptools |	An easy-install package to facilitate installing Python packages
sqlalchemy | ORM and SQL tools for Python
flask |	Microframework for web applications
python-psycopg2 | PostgreSQL adapter for Python
oauth2 | Authorization framework for third-party login (Google and Facebook)
google-api-python-client | Google API for OAuth login

### Configuration Summary

    1.  Started a new Ubuntu Linux server instance on Amazon Lightsail.
	2.  Followed the instructions provided to SSH into the server.
	       - Created a static IP and attach it to the instance in Amazon Lightsail.
		   - Opened up port 2200 on the Lightsail Networking page.
           - Used the default key pair from Lightsail to ssh into the server.
             (You will be connected as user ubuntu)
		   - Changed port 22 to 2200 in /etc/ssh/sshd_config file.	 
    3.  Created a user grader permission to sudo.
	4.  Created an SSH key pair for grader using the ssh-keygen tool.
	5.  Updated all currently installed packages.
    6.  Configured UFW to only allow incoming connections for 
		   - SSH(Port:2200), HTTP(Port:80) and NTP(Port:123).
    7.  Configured local Time Zone to UTC.
	8.  Installed and configured Apache to serve a Python mod_wsgi application.
    9.  Installed Git and Setup directory structure for delopying Flask Application.
    10. Installed and configured PostgreSQL with default settings to not allow remote connection.
	11. Created a new user catalog, added the user to PostgreSQL databse with limited permissions 
	    to the catalog database.
    12. Cloned and setup the Item Catalog project from the Github repository.
	13. Setup the app in the server so that it functions correctly when visiting the server’s IP 
	    address in a browser. 
	14. Enabled third party authentication (Google and Facebook). 	   
	
### References
    
    * Udacity's Linux Server Configuration
	* FLASK Documentation
	* SQLAlchemy documentation
    * PostgreSQL documentation
	* Digital Ocean tutorials
	* UFW - Community Help Wiki
	* NERDERATIBLOG - Simplify Your Life With an SSH Config File
	* GoDaddy Blog
	* Lightsail Documentation
	* Udacity Discussion Forum	