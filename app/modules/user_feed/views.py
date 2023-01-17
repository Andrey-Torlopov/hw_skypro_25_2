from crypt import methods
from flask import Blueprint, render_template

from app.modules.app_dao import AppDAO

userfeed_blueprint = Blueprint('userfeed_blueprint', __name__, template_folder='templates', url_prefix='/users')

appDao = AppDAO('./static/data/posts.json','./static/data/bookmarks.json','./static/data/comments.json')

@userfeed_blueprint.route('/<username>')
def show_users_posts(username):
    if len(username) == 0:
        return ""
    
    posts = appDao.get_post_by_name(username)
    return render_template("user_feed.html", username=username, posts=posts)