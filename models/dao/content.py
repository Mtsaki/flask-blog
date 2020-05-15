from datetime import datetime
from blog.database import db

class Content(db.Model):
    __tablename__ = 'content'

    content_id = db.Column(db.Integer, primary_key=True, nullable=True, unique=False)
    content_title = db.Column(db.String, nullable=False)
    image_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, nullable=False) # 0:public, 1:private
    description = db.Column(db.String, nullable=False)
    content_text = db.Column(db.String, nullable=False)
    last_update_date = db.Column(db.String, nullable=True)

    def __init__(self, content_title, image_id, category_id, status, description, content_text):
        self.content_id = None
        self.content_title = content_title
        self.image_id = image_id
        self.category_id = category_id
        self.status = status
        self.description = description
        self.content_text = content_text
        self.last_update_date = datetime.now().strftime('%Y-%m-%d')


def load_content(content_id):
    return db.session.query(Content).filter(Content.content_id == content_id).first()
    
def load_content_all():
    contents = db.session.query(Content).all()
    if contents == None:
        return []
    else:
        return contents

def insert(content_title, image_id, category_id, status, description, content_text):
    content = Content(content_title, image_id, category_id, status, description, content_text)
    db.session.add(content)
    db.session.commit()
    return content.content_id

def update(content_id, content_title, image_id, category_id, status, description, content_text):
    content = load_content(content_id)
    content.content_title = content_title
    content.image_id = image_id
    content.category_id = category_id
    content.status = status
    content.description = description
    content.content_text = content_text
    content.last_update_date = datetime.now().strftime('%Y-%m-%d')
    db.session.commit()

def delete(content_id):
    content = load_content(content_id)
    db.session.delete(content)
    db.session.commit()

