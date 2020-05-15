from flask import current_app
from werkzeug.utils import secure_filename
from blog.models import forms
from blog.models.dao import content, content_tag, category, tag, image

def load_image(image_id):
    return image.load_image(image_id)

def load_image_all_without_binary():
    return image.load_image_all_without_binary()

def add_image(form):
    image_file = form.image_file.data
    image.insert(secure_filename(image_file.filename), form.description.data, image_file.read())

def add_content(form):
    content_id = content.insert(form.content_title.data, form.image_id.data,
                                form.category_id.data, form.status.data,
                                form.description.data, form.content_text.data)
    
    for tag in form.tag.data:
        content_tag.insert(content_id, tag)

def update_content(form):
    content.update(form.content_id.data, form.content_title.data,
                    form.image_id.data, form.category_id.data,
                    form.status.data, form.description.data,
                    form.content_text.data)
    
    content_tag.delete(form.content_id.data)
    for tag in form.tag.data:
        content_tag.insert(form.content_id.data, tag)

def delete_content(form):
    content.delete(form.content_id.data)
    content_tag.delete(form.content_id.data)

def load_choices(form):
    form.image.choices = [(i.image_id, i.description) for i in image.load_image_all_without_binary()]
    form.category.choices = [(c.category_id, c.category) for c in category.load_category_all()]
    form.tags.choices = [(t.tag_id, t.tag) for t in tag.load_tag_all()]

def load_content(content_id, form):
    c = content.load_content(content_id)
    
    form.content_id.data = c.content_id
    form.content_title = c.content_title
    form.image_id = c.image_id
    form.category_id.data = c.category_id
    form.tags.data = [ tag.tag_id for tag in content_tag.load_by_content_id(content_id)]
    form.status.data = c.status
    form.description.data = c.description
    form.content_text = c.content_text
