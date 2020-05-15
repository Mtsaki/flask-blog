from flask import abort, Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required, current_user

from blog.models import forms, posting_service
from blog.models.dao import image

bp = Blueprint("post", __name__)

@bp.route("/post/image",methods=['GET','POST'])
@login_required
def add_image():
    f = forms.ImageForm()
    if f.validate_on_submit():
        posting_service.add_image(f)
        return redirect(url_for('show.index'))

    else:
        return render_template('post_image.html', form=f)

@bp.route("/post/content",methods=['GET','POST'])
@login_required
def add_content():
    f = forms.ContentForm()
    posting_service.load_choices(f)
    if f.validate_on_submit():
        posting_service.add_content(f)
        return redirect(url_for('show.content_index'))

    else:
        return render_template('post_content.html', form=f)

@bp.route("/post/content/<int:content_id>",methods=['GET','POST'])
@login_required
def edit_content(content_id):
    f = forms.ContentForm()
    posting_service.load_choices(f)
    #Delete
    if f.delete.data:
        posting_service.delete_content(f)
        return redirect(url_for('show.content_index'))

    # Update
    if f.validate_on_submit():
        posting_service.update_content(f)
        return redirect(url_for('show.one_content', content_id=content_id))

    else:
        posting_service.load_content(content_id, f)
        return render_template('post_content.html', form=f, is_update=True)
