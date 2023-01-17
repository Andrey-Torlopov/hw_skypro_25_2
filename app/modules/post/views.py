from flask import Blueprint, request, render_template
from app.modules.app_dao import AppDAO
from app.models.post import Post
from app.models.comment import Comment

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates', url_prefix='/post')

appDao = AppDAO('./static/data/posts.json','./static/data/bookmarks.json','./static/data/comments.json')

@post_blueprint.route('/<int:id>')
def page_index(id):
    post = appDao.get_post_by_id(id)
    if post is None:
        return ""
    return render_template("post.html", post=post)