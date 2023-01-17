import os
import dotenv
from flask import Flask
from flask import render_template

from app.modules.app_dao import AppDAO
from app.modules.main.views import main_blueprint
from app.modules.post.views import post_blueprint
from app.modules.user_feed.views import userfeed_blueprint
from app.modules.api.views import api_blueprint

import app.modules.app_dao as app_dao

app = Flask(__name__)

dotenv.load_dotenv(override=True)
if os.environ.get("APP_CONFIG") == "development":
    app.config.from_pyfile('config/development.py')
else:
    app.config.from_pyfile('config/production.py')
    
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(userfeed_blueprint)
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")

@app.errorhandler(500)
def not_found(e):
  return render_template("500.html")


if __name__ == "__main__":
    app.debug = True
    app.run()


