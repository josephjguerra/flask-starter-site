# flask-starter-site
* basic [flask](http://flask.pocoo.org/) site with user login and [bootstrap](http://getbootstrap.com/) for rapid python web app prototyping
* check out [Treehouse](https://teamtreehouse.com/) for some great flask tutorials. They eventually led me to this repo!
* these steps are for Mac OS X
* this uses a [SQLite](https://www.sqlite.org/) and [peewee](https://github.com/coleifer/peewee). A good tool for prototyping. Probably not production :)

### make a virtual environment
* `mkdir my-flask-projects`
* `cd my-flask-projects`
* `python -m venv flask-venv`
* `source flask-venv/bin/activate`

### get the code into a directory
* `git clone https://github.com/josephjguerra/flask-starter-site.git`

### get the required packages
* `pip install peewee`
* `pip install flask`
* `pip install flask-login`
* `pip install flask-bcrypt`
* `pip install flask-wtf`

### see the app!
* `cd flask-starter-site`
* `python app.py`
* go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the starter site!
* register a user (or a few)
* login

### now what?
* learn more about [flask](http://flask.pocoo.org/)
* expand this starter site to prototype your next big idea
* try connecting a real database
* host your project on:
  - [pythonanywhere](https://www.pythonanywhere.com/) - my preference
  - [Heroku](https://www.heroku.com/) - also straightforward with heroku toolbelt
  - [DigitalOcean](https://www.digitalocean.com/)
  - [AWS](https://aws.amazon.com/)
* the sky's the limit!

### cleaning up
* `control + C ` will stop the app from running
* `deactivate` in your `my-flask-projects` directory to stop your virtual environment
