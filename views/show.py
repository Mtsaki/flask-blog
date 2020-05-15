import os
from flask import Blueprint, render_template, make_response

from blog.models import posting_service
from blog.models.dao import content

bp = Blueprint("show", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/content")
def content_index():
    c = content.load_content_all()
    return render_template("content_index.html", contents=c)

@bp.route("/content/<int:content_id>")
def one_content(content_id):
    c = content.load_content(content_id)
    return render_template("content.html", content=c)

@bp.route("/about")
def about():
    return render_template("about.html")


@bp.route("/image/<int:image_id>")
def load_image(image_id):
    image = posting_service.load_image(image_id)
    response = make_response()
    response.data = image.image_file
    response.headers['Content-Disposition'] = 'attachment; filename=' + image.file_name
    root, ext = os.path.splitext(image.file_name)
    response.mimetype = 'image/' + ext
    return response


@bp.errorhandler(404)
def error_handler(error):
    msg = 'Error: {code}\n'.format(code=error.code)
    return msg, error.code