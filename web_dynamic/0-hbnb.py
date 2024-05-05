#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, url_for
from models import storage
import uuid;

#FLASK setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

#being Flask page rendering

@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/0-hbnb')
def hbnb_filters(id=None):
    """ Display a HTML page: 6-index.html """
    states_obj = storage.all("State")
    states = dict([state.name, state] for state in states_obj)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=states,
                           amens=amens,
                           places=places,
                           users=users)

if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
