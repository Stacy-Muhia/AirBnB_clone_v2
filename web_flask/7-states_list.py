#!/usr/bin/python3
""" Functions to start a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
from flask import Flask, render_template
from models import storage
from models.state import State


@app.teardown_appcontext
def close_db(error):
    """ Removing the current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displaying a HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
