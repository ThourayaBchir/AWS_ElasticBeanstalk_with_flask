from flask import Flask

# EB looks for an 'application' callable by default.
application = Flask(__name__)

from application import routes
