from crypt import methods
import json
from flask import Blueprint, jsonify
import logging

from app.modules.app_dao import AppDAO

api_blueprint = Blueprint('api_blueprint', __name__)

appDao = AppDAO('./static/data/posts.json','./static/data/bookmarks.json','./static/data/comments.json')

@api_blueprint.route('/api/posts', methods=['GET'])
def api_get_posts():
    posts = appDao.load_posts()
    logging.info('Запрос: api/posts')
    return jsonify(posts)

@api_blueprint.route("/api/post/<int:id>")
def api_get_post(id):
    logging.info(f'Запрос: api/post/{id}')
    post = appDao.get_post_by_id(id)
    if post is None:
        return {"status": "fail"}
    return jsonify(post)

