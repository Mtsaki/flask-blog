from blog.database import db

class ContentTag(db.Model):
    __tablename__ = 'tag'

    content_id = db.Column(db.Integer, primary_key=True, nullable=True)
    tag_id = db.Column(db.Integer, primary_key=True, nullable=True)
    
    def __init__(self, content_id, tag_id):
        self.content_id = content_id
        self.tag_id = tag_id
        
def load_by_content_id(content_id):
    return db.session.query(ContentTag).filter(ContentTag.content_id == content_id)
    
def load_by_tag_id(tag_id):
    return db.session.query(ContentTag).filter(ContentTag.tag_id == tag_id)

def insert(content_id, tag_id):
    content_tag = ContentTag(content_id, tag_id)
    db.session.add(content_tag)
    db.session.commit()

def delete(content_id):
    content_tag = load_by_content_id(content_id)
    content_tag.delete()
    db.session.commit()