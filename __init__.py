from flask import Flask

# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)


 
from . import auth
app.register_blueprint(auth.bp)

from . import careers
app.register_blueprint(careers.bp)

app.add_url_rule('/', endpoint='index')

