# Embedded Smart Home 2017 - Web GUI
A simple webserver that can be used as a GUI for a smarthome environment based on Python with Flask. Designed to be used in the OpenHPI course [Embedded Smart Home 2017](https://open.hpi.de/courses/smarthome2017). Licensed under MIT, see LICENSE for more information.

## Installation and Setup
### Prerequisites
- Have python3 installed (`sudo apt install python3`)
- Have pip3 installed (`sudo apt install python3-pip`)
- We recommend doing this in a new virtual environment. To achieve that, first install the python package virtualenv if you haven't already done that: `sudo pip3 install virtualenv`. Afterwards, create a virtual environment with `virtualenv venv`. You can activate it with `. venv/bin/activate`. To deactivate it, use `deactivate`

### Installing Flask and Flask's Bootstrap extension
Now, we can install the flask and flask-bootstrap packages. To do this, use: `sudo pip3 install flask flask-bootstrap`.

## Running the server
We have to export the main program to an environment variable so Flask knows where to search: `export FLASK_APP=smarthome.py`. Afterwards, start Flask: `python3 -m flask run`

You will see the logging output of the server. Open your web browser and go to `http://localhost:5000` to see the webpage. Press `Ctrl + C` to leave.

## Security Concerns
By default, the Flask server is only visible on your local machine. To change that, take a look at the flask documentation, understand why they did it and do the changes they list. If you don't know what you're doing, leave everything the way it is since you might open your computer to remote code execution.
